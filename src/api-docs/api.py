from fastapi import FastAPI

from src.retriever import Retriever
from src.generator import generate_answer


app = FastAPI(
    title="Engineering Knowledge RAG"
)

retriever = Retriever()


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask(question: str):

    results = retriever.search(
        question,
        top_k=3
    )

    answer = generate_answer(
        question,
        results
    )

    return {
        "question": question,
        "answer": answer,
        "sources": [
            result["source"]
            for result in results
        ]
    }