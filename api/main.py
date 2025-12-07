import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from openai import OpenAI
import qdrant_client

app = FastAPI()

class ChatRequest(BaseModel):
    query: str
    context_text: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    query_to_embed = request.query
    if request.context_text:
        query_to_embed = f"{request.context_text}\n\n{request.query}"

    response = openai_client.embeddings.create(
        input=query_to_embed,
        model="text-embedding-3-small"
    )
    query_vector = response.data[0].embedding

    qdrant = qdrant_client.QdrantClient(
        url=os.environ.get("QDRANT_URL"), 
        api_key=os.environ.get("QDRANT_API_KEY")
    )
    
    search_result = qdrant.search(
        collection_name="book_content_v1",
        query_vector=query_vector, 
        limit=5
    )
    
    context = ""
    sources = set()
    for hit in search_result:
        context += hit.payload['text'] + "\n---\n"
        sources.add(hit.payload['metadata']['source'])

    prompt = f"""
You are a helpful assistant for the book "The Guide to Modern Agentic Development: Physical AI and Humanoid Robotics".
Answer the user's question based only on the following context.
Cite the sources you used to answer the question.
This is a Context7 framework application.

Context:
{context}

Question: {request.query}

Answer:
    """

    chat_completion = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4-turbo",
    )
    
    answer = chat_completion.choices[0].message.content

    return ChatResponse(
        answer=answer,
        sources=list(sources)
    )
