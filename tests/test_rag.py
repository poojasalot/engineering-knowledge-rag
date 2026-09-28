from src.retriever import Retriever


def test_authentication_retrieval():
    retriever = Retriever()

    results = retriever.search(
        "What should I consider before changing authentication?"
    )

    assert results

    sources = [
        result["source"]
        for result in results
    ]

    assert "authentication.md" in sources


def test_deployment_retrieval():
    retriever = Retriever()

    results = retriever.search(
        "How should I deploy a high-risk change?"
    )

    assert results

    sources = [
        result["source"]
        for result in results
    ]

    assert "deployment.md" in sources