import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from typing import List, Optional
from openai import OpenAI
import qdrant_client
from openai_chatkit import ChatKit

# Initialize FastAPI app
app = FastAPI()

# --- Environment Variables & Clients ---
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
QDRANT_URL = os.environ.get("QDRANT_URL")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")
CHATKIT_SECRET_KEY = os.environ.get("CHATKIT_SECRET_KEY") # This is a new required secret

# Ensure all necessary environment variables are set
if not all([OPENAI_API_KEY, QDRANT_URL, QDRANT_API_KEY, CHATKIT_SECRET_KEY]):
    raise ValueError("One or more required environment variables are not set.")

# Initialize clients
openai_client = OpenAI(api_key=OPENAI_API_KEY)
qdrant_client_instance = qdrant_client.QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)
chatkit = ChatKit(secret_key=CHATKIT_SECRET_KEY)

# --- Pydantic Models ---
class SessionRequest(BaseModel):
    user_id: str

class SessionResponse(BaseModel):
    client_secret: str

class ChatRequest(BaseModel):
    query: str
    context_text: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

# --- ChatKit Tool: Qdrant Vector Search ---
@chatkit.tool()
def retrieve_context(query: str, context_text: Optional[str] = None) -> str:
    """
    Retrieves relevant context from the Qdrant vector database based on the user's query.
    """
    query_to_embed = f"{context_text}\n\n{query}" if context_text else query
    
    response = openai_client.embeddings.create(
        input=query_to_embed,
        model="text-embedding-3-small"
    )
    query_vector = response.data[0].embedding

    search_result = qdrant_client_instance.search(
        collection_name="book_content_v1",
        query_vector=query_vector,
        limit=5
    )

    context = ""
    sources = set()
    for hit in search_result:
        context += hit.payload['text'] + "\n---\n"
        sources.add(hit.payload['metadata']['source'])

    # The context string now includes the source references
    source_references = "\n\nSources:\n" + "\n".join(f"- {source}" for source in sources)
    return context + source_references

# --- ChatKit Assistant Definition ---
ASSISTANT_ID = "book-rag-assistant" # Define a unique ID for the assistant

@chatkit.assistant(id=ASSISTANT_ID)
async def rag_assistant(message: str, tools: list):
    """
    A RAG assistant that answers questions about the book.
    """
    system_prompt = f"""
You are a helpful assistant for the book "The Guide to Modern Agentic Development: Physical AI and Humanoid Robotics".
Answer the user's question based only on the context provided by the `retrieve_context` tool.
Cite the sources you used to answer the question as provided at the end of the context.
This is a Context7 framework application.
    """
    
    # Use the tool to get context
    context = await tools.retrieve_context(query=message)
    
    # Construct the final prompt for the LLM
    final_prompt = f"Context:\n{context}\n\nQuestion: {message}\n\nAnswer:"
    
    chat_completion = openai_client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": final_prompt},
        ],
        model="gpt-4-turbo",
    )
    
    return chat_completion.choices[0].message.content

# --- API Endpoints ---
@app.post("/api/chatkit/session", response_model=SessionResponse)
async def create_chatkit_session(request: SessionRequest):
    """
    Generates a short-lived Client Secret for a user to authenticate with ChatKit.
    """
    try:
        session = await chatkit.sessions.create(user_id=request.user_id)
        return SessionResponse(client_secret=session.client_secret)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create ChatKit session: {str(e)}")

# Mount the ChatKit app to the FastAPI instance
app.mount("/api/chat", chatkit.to_asgi())

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to the RAG Chatbot API"}

# Note: The original /api/chat endpoint is now replaced by the ChatKit ASGI app.
# ChatKit will handle the /api/chat route for all its interactions.
# The `rag_assistant` will be invoked by ChatKit when a user sends a message.