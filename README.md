# engineering-knowledge-rag

A Retrieval-Augmented Generation (RAG) starter repository for engineering knowledge: ingest docs, build a vector index, and serve answers augmented by retrieved context.

## Contents
- README — this file  
- src/ — core ingestion, embedding, indexing, and API code  
- docs/ — raw and processed documents

## Features
- Document ingestion (PDF, Markdown, HTML, plain text)  
- Chunking and metadata extraction (titles, source, timestamps)  
- Embeddings via pluggable providers (OpenAI, HuggingFace, etc.)  
- Vector stores supported (FAISS, Milvus, Weaviate — configurable)  
- Simple query API that returns retrieved context + LLM answer  
- Evaluation utilities (retrieval metrics, answer traces)

## Quickstart (local)
1. Clone:
    ```
    git clone <repo-url>
    cd engineering-knowledge-rag
    ```
2. Create venv and install:
    ```
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
3. Configure env (example):
    ```
    export EMBEDDING_PROVIDER=openai
    export OPENAI_API_KEY=sk_...
    export VECTOR_STORE=faiss
    ```
4. Ingest documents:
    ```
    python src/ingest.py --input data/raw --output data/processed
    ```
5. Run API:
    ```
    uvicorn src.api:app --reload
    ```
6. Query:
    POST /ask with JSON { "q": "How does X work?" }


## Testing & CI
- Unit tests: `pytest -m tests/`  
