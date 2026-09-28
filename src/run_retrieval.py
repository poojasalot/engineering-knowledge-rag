from retriever import Retriever


retriever = Retriever()

query = "What should I do before deploying a risky authentication change?"

results = retriever.search(query)


print("\nQUESTION:")
print(query)

print("\nRETRIEVED CONTEXT:")

for result in results:
    print("\n----------------------------")
    print(f"Source: {result['source']}")
    print(f"Score: {result['score']:.4f}")
    print(result["content"])