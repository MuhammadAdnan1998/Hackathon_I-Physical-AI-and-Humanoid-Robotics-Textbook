import os
import re
import json
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

# --- Configuration ---
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION_NAME = "book_content_v1"
DOCS_DIR = "docs"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
# Max characters per chunk. Adjust based on model context window and desired granularity.
CHUNK_SIZE = 500
# Overlap between chunks to maintain context.
CHUNK_OVERLAP = 50

# Initialize Markdown parser
md = MarkdownIt()

def get_qdrant_client():
    """Initializes and returns a Qdrant client."""
    return QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT, api_key=QDRANT_API_KEY)

def get_embedding_model():
    """Loads and returns the Sentence Transformer model."""
    return SentenceTransformer(EMBEDDING_MODEL_NAME)

def parse_markdown_content(filepath: str) -> str:
    """
    Parses a markdown or mdx file, extracts text, and strips front matter and JSX.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip front matter (Jekyll/Docusaurus style: --- ... ---
    content = re.sub(r'^---\n(.*?)\n---\n', '', content, flags=re.DOTALL)

    # Convert markdown to HTML first to easily strip JSX and get clean text
    html = md.render(content)

    # Use BeautifulSoup to strip HTML tags and any remaining JSX-like elements
    soup = BeautifulSoup(html, 'html.parser')

    # Remove code blocks and other elements that shouldn't be embedded as prose
    for tag in soup.find_all(['code', 'pre', 'script', 'style']):
        tag.decompose()

    clean_text = soup.get_text()

    # Remove any remaining JSX or shortcodes that BeautifulSoup might miss
    clean_text = re.sub(r'{%.*?%}', '', clean_text)  # Docusaurus/Jekyll shortcodes
    clean_text = re.sub(r'{.*?}', '', clean_text)    # Generic JSX-like
    clean_text = re.sub(r'<[A-Z][a-zA-Z0-9]*\s*/>', '', clean_text) # Self-closing JSX
    clean_text = re.sub(r'<[A-Z][a-zA-Z0-9]*[^>]*>.*?</[A-Z][a-zA-Z0-9]*>', '', clean_text, flags=re.DOTALL) # JSX components

    return clean_text.strip()

def chunk_text(text: str, filepath: str) -> list[dict]:
    """
    Splits text into chunks with overlap and attaches metadata.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        
        # Add metadata for citation
        metadata = {
            "source": filepath,
            "start_char": start,
            "end_char": end,
            # Add more metadata if available, e.g., title, section
        }
        chunks.append({"text": chunk, "metadata": metadata})
        
        start += (CHUNK_SIZE - CHUNK_OVERLAP)
        if CHUNK_OVERLAP <= 0 and start < len(text):
            start = end # Move to the end if no overlap

    return chunks

def scan_docs_for_markdown(docs_dir: str) -> list[str]:
    """
    Scans the docs directory for all .md and .mdx files.
    """
    markdown_files = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith((".md", ".mdx")):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def main():
    print(f"Scanning '{DOCS_DIR}' for markdown files...")
    markdown_files = scan_docs_for_markdown(DOCS_DIR)
    print(f"Found {len(markdown_files)} markdown files.")

    if not markdown_files:
        print("No markdown files found to process. Exiting.")
        return

    qdrant_client = get_qdrant_client()
    embedding_model = get_embedding_model()
    
    # Ensure collection exists and has correct config
    try:
        qdrant_client.recreate_collection(
            collection_name=QDRANT_COLLECTION_NAME,
            vectors_config=models.VectorParams(size=embedding_model.get_sentence_embedding_dimension(), distance=models.Distance.COSINE),
        )
        print(f"Collection '{QDRANT_COLLECTION_NAME}' recreated successfully.")
    except Exception as e:
        print(f"Could not recreate collection, might already exist or error: {e}")
        # If recreate fails, try to get current config to verify
        try:
            collection_info = qdrant_client.get_collection(collection_name=QDRANT_COLLECTION_NAME).config
            if collection_info.params.vectors.size != embedding_model.get_sentence_embedding_dimension():
                print(f"Warning: Collection vector size mismatch. Expected {embedding_model.get_sentence_embedding_dimension()}, got {collection_info.params.vectors.size}.")
                print("Please consider deleting and recreating the collection manually if issues persist.")
        except Exception as e_get:
            print(f"Could not retrieve collection info: {e_get}. Please ensure Qdrant is running and accessible.")
            return


    all_points = []
    for filepath in markdown_files:
        print(f"Processing '{filepath}'...")
        clean_text = parse_markdown_content(filepath)
        chunks = chunk_text(clean_text, filepath)
        
        for chunk_data in chunks:
            chunk_text = chunk_data["text"]
            metadata = chunk_data["metadata"]
            
            embedding = embedding_model.encode(chunk_text).tolist()
            
            all_points.append(
                models.PointStruct(
                    id=None, # Qdrant will assign ID
                    vector=embedding,
                    payload={"content": chunk_text, **metadata}
                )
            )
            
            if len(all_points) >= 100: # Batch upload for efficiency
                print(f"Uploading batch of {len(all_points)} points...")
                qdrant_client.upsert(
                    collection_name=QDRANT_COLLECTION_NAME,
                    wait=True,
                    points=all_points
                )
                all_points = []
    
    # Upload any remaining points
    if all_points:
        print(f"Uploading final batch of {len(all_points)} points...")
        qdrant_client.upsert(
            collection_name=QDRANT_COLLECTION_NAME,
            wait=True,
            points=all_points
        )
    
    print("Vectorization complete.")

if __name__ == "__main__":
    main()
