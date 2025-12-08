import os
import httpx
import openai
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional
from qdrant_client import QdrantClient
from openai_chatkit import ChatKit

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    openai_api_key: SecretStr
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: SecretStr
    chatkit_secret_key: SecretStr

class Context:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.http_client: httpx.AsyncClient | None = None
        self.qdrant_client: QdrantClient | None = None
        self.openai_client: openai.AsyncOpenAI | None = None
        self.chatkit: ChatKit | None = None

    async def startup(self):
        self.http_client = httpx.AsyncClient()
        self.qdrant_client = QdrantClient(
            self.settings.qdrant_url,
            api_key=self.settings.qdrant_api_key.get_secret_value(),
        )
        self.openai_client = openai.AsyncOpenAI(
            api_key=self.settings.openai_api_key.get_secret_value()
        )
        self.chatkit = ChatKit(secret_key=self.settings.chatkit_secret_key.get_secret_value())

    async def shutdown(self):
        if self.http_client:
            await self.http_client.aclose()
        if self.openai_client:
            # an issue with openai client that it hangs on shutdown, so we are not closing it
            # await self.openai_client.close()
            pass

def get_fast_api_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title="AI-Tutor API",
        version="0.1.0",
        description="AI-Tutor API",
        debug=settings.debug,
    )

    @app.on_event("startup")
    async def startup():
        context = Context(settings)
        await context.startup()
        app.state.context = context

    @app.on_event("shutdown")
    async def shutdown():
        context: Context = app.state.context
        await context.shutdown()

    # app.include_router(chat.router, prefix="/chat", tags=["chat"])

    return app

settings = Settings()
app = get_fast_api_app(settings)

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
@app.state.context.chatkit.tool()
def retrieve_context(query: str, context_text: Optional[str] = None) -> str:
    """
    Retrieves relevant context from the Qdrant vector database based on the user's query.
    """
    query_to_embed = f"{context_text}\n\n{query}" if context_text else query
    
    response = app.state.context.openai_client.embeddings.create(
        input=query_to_embed,
        model="text-embedding-3-small"
    )
    query_vector = response.data[0].embedding

    search_result = app.state.context.qdrant_client.search(
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

@app.state.context.chatkit.assistant(id=ASSISTANT_ID)
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
    
    chat_completion = await app.state.context.openai_client.chat.completions.create(
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
        session = await app.state.context.chatkit.sessions.create(user_id=request.user_id)
        return SessionResponse(client_secret=session.client_secret)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create ChatKit session: {str(e)}")

# Mount the ChatKit app to the FastAPI instance
app.mount("/api/chat", app.state.context.chatkit.to_asgi())

@app.get("/")
def read_root():
    return {"Hello": "World", "message": "Welcome to the RAG Chatbot API"}

