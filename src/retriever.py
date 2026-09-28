import numpy as np
from sentence_transformers import SentenceTransformer



from src.ingest import load_documents


class Retriever:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.documents = load_documents()

        self.embeddings = self.model.encode(
            [document["content"] for document in self.documents]
        )

    def cosine_similarity(self, a, b):
        """
        Calculate cosine similarity between two vectors.
        
        Args:
            a: First vector
            b: Second vector
            
        Returns:
            float: Cosine similarity score between -1 and 1.
                   Returns 0 if either vector is zero.
        """
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        
        # Handle edge case: zero vectors have no similarity
        if norm_a == 0 or norm_b == 0:
            return 0.0
        
        return np.dot(a, b) / (norm_a * norm_b)

    def search(self, query: str, top_k: int = 3, min_score: float = 0.25):
        query_embedding = self.model.encode(query)
        results = []

        for document, embedding in zip(self.documents, self.embeddings):
            score = self.cosine_similarity(query_embedding, embedding)

            if score >= min_score:
                results.append({
                    "score": float(score),
                    "source": document["source"],
                    "chunk_id": document["chunk_id"],
                    "content": document["content"],
                })

        results.sort(key=lambda x: x["score"], reverse=True)

        return results[:top_k]

