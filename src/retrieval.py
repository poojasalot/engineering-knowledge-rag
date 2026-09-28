from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer("all-MiniLM-L6-v2")


documents = [
    "Authentication changes require additional production validation.",
    "Deploy high-risk changes using a gradual canary rollout.",
    "Incident response should focus first on restoring customer impact.",
    "Database migrations should be carefully validated before production.",
]

query = "What should I do before deploying a risky authentication change?"

document_embeddings = model.encode(documents)
query_embedding = model.encode(query)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


scores = []

for document, embedding in zip(documents, document_embeddings):
    score = cosine_similarity(query_embedding, embedding)
    scores.append((score, document))


scores.sort(reverse=True)


print("\nQuery:")
print(query)

print("\nMost relevant documents:")

for score, document in scores:
    print(f"{score:.4f} - {document}")