from pathlib import Path
from src.chunker import chunk_text



DOCS_DIR = Path("docs")


def load_documents():
    documents = []

    for file_path in DOCS_DIR.glob("*.md"):
        text = file_path.read_text()

        chunks = chunk_text(text)

        for index, chunk in enumerate(chunks):
            documents.append({
                "source": file_path.name,
                "chunk_id": index,
                "content": chunk,
            })

    return documents


if __name__ == "__main__":
    documents = load_documents()

    print(f"Loaded {len(documents)} chunks")

    for document in documents:
        print(
            f"{document['source']} "
            f"(chunk {document['chunk_id']}): "
            f"{document['content'][:100]}..."
        )