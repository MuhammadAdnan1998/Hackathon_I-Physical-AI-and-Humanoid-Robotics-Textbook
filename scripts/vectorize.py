import os
import uuid
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from openai import OpenAI
import qdrant_client
from qdrant_client.http import models

def upload_to_qdrant(client, collection_name, chunks_with_embeddings):
    """
    Uploads vectors and payloads to a Qdrant collection.
    """
    points = []
    for chunk in chunks_with_embeddings:
        points.append(models.PointStruct(
            id=str(uuid.uuid4()),
            vector=chunk['vector'],
            payload={
                "text": chunk['text'],
                "metadata": chunk['metadata']
            }
        ))
    
    client.upsert(
        collection_name=collection_name,
        wait=True,
        points=points
    )
    print(f"Uploaded {len(points)} points to '{collection_name}'.")

def create_qdrant_collection(client, collection_name, vector_size):
    """
    Creates a Qdrant collection if it doesn't exist.
    """
    try:
        client.get_collection(collection_name=collection_name)
        print(f"Collection '{collection_name}' already exists.")
    except Exception:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        )
        print(f"Collection '{collection_name}' created.")

def qdrant_connect():
    """
    Connects to Qdrant Cloud.
    """
    client = qdrant_client.QdrantClient(
        url=os.environ.get("QDRANT_URL"), 
        api_key=os.environ.get("QDRANT_API_KEY")
    )
    return client

def generate_embeddings(chunks):
    """
    Generates embeddings for a list of text chunks using OpenAI.
    """
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    for chunk in chunks:
        response = client.embeddings.create(
            input=chunk['text'],
            model="text-embedding-3-small"
        )
        chunk['vector'] = response.data[0].embedding
    return chunks

def chunk_text(text, metadata, chunk_size=750, overlap=100):
    """
    Splits the text into smaller chunks with a specified size and overlap.
    Each chunk is a dictionary containing the text and its metadata.
    """
    if not text:
        return []
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk_data = {
            'text': text[start:end],
            'metadata': metadata
        }
        chunks.append(chunk_data)
        start += chunk_size - overlap
    return chunks

def parse_markdown(file_path):
    """
    Parses a Markdown/MDX file, removes front matter and JSX,
    and returns clean, readable text.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple front matter removal
    parts = content.split('---')
    if len(parts) > 2:
        content = '---'.join(parts[2:])

    # Render Markdown to HTML
    md = MarkdownIt()
    html = md.render(content)

    # Extract text from HTML, removing JSX-like tags
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()

    # Get text
    text = soup.get_text()

    # Break into lines and remove leading/trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

def scan_documents(doc_path='docs'):
    """
    Scans the given directory for .md and .mdx files.
    """
    found_files = []
    for root, _, files in os.walk(doc_path):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                found_files.append(os.path.join(root, file))
    return found_files

if __name__ == '__main__':
    COLLECTION_NAME = "book_content_v1"
    VECTOR_SIZE = 1536

    files = scan_documents()
    all_chunks = []
    for f in files:
        print(f"--- Parsing {f} ---")
        clean_text = parse_markdown(f)
        metadata = {'source': f}
        text_chunks = chunk_text(clean_text, metadata)
        all_chunks.extend(text_chunks)
        print(f"Found {len(text_chunks)} chunks.")

    print("\nGenerating embeddings...")
    chunks_with_embeddings = generate_embeddings(all_chunks)
    print("Embeddings generated.")

    print("\nConnecting to Qdrant...")
    qdrant = qdrant_connect()
    print("Connected to Qdrant.")

    print(f"\nCreating Qdrant collection '{COLLECTION_NAME}'...")
    create_qdrant_collection(qdrant, COLLECTION_NAME, VECTOR_SIZE)

    print("\nUploading to Qdrant...")
    upload_to_qdrant(qdrant, COLLECTION_NAME, chunks_with_embeddings)
    
    print("\nDone.")