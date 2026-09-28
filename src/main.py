from src.retriever import Retriever
from src.generator import generate_answer


def main():

    question = input("\nAsk an engineering question: ")

    retriever = Retriever()

    results = retriever.search(
        question,
        top_k=3
    )

    print("\n==============================")
    print("RETRIEVED DOCUMENTS")
    print("==============================")

    for result in results:
        print("\n----------------------------")
        print(f"Source: {result['source']}")
        print(f"Score: {result['score']:.4f}")
        print(result["content"])

    

    answer = generate_answer(
        question,
        results
    )

    print("\n==============================")
    print("ENGINEERING KNOWLEDGE ASSISTANT")
    print("==============================")

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for result in results:
        print(
            f"- {result['source']} "
            f"(similarity={result['score']:.4f})"
        )


if __name__ == "__main__":
    main()