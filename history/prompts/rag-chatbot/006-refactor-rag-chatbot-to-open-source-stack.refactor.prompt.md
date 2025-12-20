---
id: 006
title: Refactor RAG Chatbot to Open Source Stack
stage: refactor
date: 2025-12-20
surface: agent
model: gemini-pro
feature: rag-chatbot
branch: main
user: 
command: 
labels: [rag, huggingface, fastapi, refactor]
links:
  spec: specifyfiles/.specify/memory/spec.md#RAG-Chatbot-Integration-Feature
  ticket: null
  adr: null
  pr: null
files:
  - specifyfiles/.specify/memory/spec.md
  - specifyfiles/.specify/memory/plan.md
tests:
  []
---

## Prompt

Review the existing "RAG Chatbot Integration Feature" in '.specify/memory/spec.md' and the plan in '.specify/memory/plan.md'.

**Replace all mention of "OpenAI Agents/ChatKit SDKs" and "OpenAI API Key" with the following architecture:**

1.  **LLM Backend:** The RAG final answer generation must use the **Hugging Face Inference API** (using a specified free-tier open-source model like Llama 3) for the LLM component.
2.  **Embedding:** The vectorization pipeline must use a **local Sentence Transformer model** (e.g., 'all-MiniLM-L6-v2' via the Hugging Face library) to generate embeddings for Qdrant, eliminating the need for a paid embedding API key.
3.  **Frontend:** The Docusaurus React component will communicate directly with the secure **FastAPI RAG endpoint** (which will now handle the full RAG pipeline without ChatKit).

Update both files to reflect this shift to an **Open-Source/Free Tier RAG Stack**, explicitly removing the need for a credit-card-required API key.

## Response snapshot

I have successfully updated both `specifyfiles/.specify/memory/spec.md` and `specifyfiles/.specify/memory/plan.md` to reflect the new open-source RAG architecture. I have replaced all mentions of OpenAI and ChatKit with a Hugging Face-powered FastAPI backend, local Sentence Transformers for embeddings, and a direct frontend-to-FastAPI communication model.

## Outcome

- ✅ Impact: High. The change fundamentally alters the architecture of the RAG chatbot feature.
- 🧪 Tests: No tests were run as this was a documentation change.
- 📁 Files: Updated the feature specification and implementation plan for the RAG chatbot.
- 🔁 Next prompts: The user might ask to start implementing the new plan.
- 🧠 Reflection: The refactoring was straightforward. The key was to systematically replace all instances of the proprietary stack with the open-source alternatives.

## Evaluation notes (flywheel)

- Failure modes observed: Initially failed to find the files due to incorrect path. Corrected the path and proceeded.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): n/a
