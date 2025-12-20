# Tasks: Open-Source RAG Chatbot Implementation

**Spec**: `specifyfiles/.specify/memory/spec.md#RAG-Chatbot-Integration-Feature`
**Plan**: `specifyfiles/.specify/memory/plan.md#RAG-Chatbot-Implementation-Plan`

This task list outlines the implementation of the RAG chatbot using an open-source stack.

---

## Phase 1: Vectorization Pipeline (Local Embeddings)

**Goal**: Create a script to process and upload the book's content to the Qdrant vector store.

- [ ] **T200**: Set up the vectorization script environment.
    - [ ] **T200.1**: Create a `requirements.txt` file in the `scripts/` directory with `qdrant-client`, `beautifulsoup4`, `markdown-it-py`, and `sentence-transformers`.
    - [ ] **T200.2**: Install the dependencies from `scripts/requirements.txt`.

- [ ] **T201**: Implement the content scraper in `scripts/vectorize.py`.
    - [ ] **T201.1**: Create a function to scan the `docs/` directory for `.md` and `.mdx` files.
    - [ ] **T201.2**: Implement logic to parse content, stripping front matter and JSX.

- [ ] **T202**: Implement text chunking in `scripts/vectorize.py`.
    - [ ] **T202.1**: Add a text splitter to break content into smaller chunks.
    - [ ] **T202.2**: Attach metadata (source file, headings) to each chunk.

- [ ] **T203**: Implement embedding generation in `scripts/vectorize.py`.
    - [ ] **T203.1**: Load the `all-MiniLM-L6-v2` Sentence Transformer model.
    - [ ] **T203.2**: Generate a vector for each text chunk.

- [ ] **T204**: Implement Qdrant vector upload in `scripts/vectorize.py`.
    - [ ] **T204.1**: Initialize the Qdrant client.
    - [ ] **T204.2**: Create a Qdrant collection named `book_content_v1` with the correct vector size (384).
    - [ ] **T204.3**: Batch-upload the vectors and metadata to the collection.
    - [ ] **T204.4**: Run the script to perform a full vectorization of the `docs/` directory.

---

## Phase 2: FastAPI Backend Service (Hugging Face RAG Pipeline)

**Goal**: Create the FastAPI backend to serve the RAG pipeline.

- [ ] **T300**: Set up the FastAPI server environment.
    - [ ] **T300.1**: Ensure `api/main.py` is set up with a basic FastAPI app.
    - [ ] **T300.2**: Create/update the `api/requirements.txt` file with `fastapi`, `uvicorn`, `qdrant-client`, `pydantic`, `sentence-transformers`, and `huggingface_hub`.
    - [ ] **T300.3**: Install the dependencies from `api/requirements.txt`.

- [ ] **T301**: Implement the RAG chat endpoint in `api/main.py`.
    - [ ] **T301.1**: Define a POST endpoint at `/api/rag/chat`.
    - [ ] **T301.2**: The endpoint should accept a JSON payload with `query` and optional `context`.

- [ ] **T302**: Implement the RAG pipeline logic in `api/main.py`.
    - [ ] **T302.1**: Load the `all-MiniLM-L6-v2` model for query embedding.
    - [ ] **T302.2**: Implement Qdrant retrieval to find relevant text chunks.
    - [ ] **T302.3**: Implement prompt construction logic.
    - [ ] **T302.4**: Implement the call to the Hugging Face Inference API.
    - [ ] **T302.5**: Return a JSON response with the answer and sources.

---

## Phase 3: Docusaurus Frontend Component (Custom React UI)

**Goal**: Integrate a custom chat UI into the Docusaurus site.

- [ ] **T400**: Set up the Chatbot component.
    - [ ] **T400.1**: Ensure the React component exists at `src/components/Chatbot/index.tsx`.

- [ ] **T401**: Build the custom chat UI.
    - [ ] **T401.1**: Implement the chat window, message list, and input field using standard React components.
    - [ ] **T401.2**: Implement state management for the conversation.
    - [ ] **T401.3**: On submit, make a `fetch` request to the `/api/rag/chat` endpoint.
    - [ ] **T401.4**: Render the response from the backend.
    - [ ] **T401.5**: Style the component to match the Docusaurus theme.

- [ ] **T402**: Implement context capture logic.
    - [ ] **T402.1**: Add a global event listener for text selection.
    - [ ] **T402.2**: Display a button to "Ask about this" for selected text.

- [ ] **T403**: Integrate the Chatbot into the site.
    - [ ] **T403.1**: Import and render the `<Chatbot />` component in `src/theme/Root.tsx`.

---

## Phase 4: Verification

**Goal**: Verify the complete open-source RAG implementation.

- [ ] **T500**: Verify the backend and vectorization.
    - [ ] **T500.1**: Run the FastAPI server.
    - [ ] **T500.2**: Send test queries to the `/api/rag/chat` endpoint and validate the responses.
- [ ] **T501**: Verify the frontend integration.
    - [ ] **T501.1**: Run the Docusaurus development server.
    - [ ] **T501.2**: Open the site and verify the chatbot UI appears correctly.
    - [ ] **T501.3**: Test the chatbot by sending messages and verifying the streamed response.
    - [ ] **T501.4**: Test the context capture feature (select text and ask).
