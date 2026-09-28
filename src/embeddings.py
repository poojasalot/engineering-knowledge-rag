from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

text = "Authentication changes require additional production validation."

embedding = model.encode(text)

print("Embedding dimensions:", len(embedding))
print("First 5 values:", embedding[:5])