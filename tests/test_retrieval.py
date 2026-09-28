from src.retriever import Retriever


def test_authentication_query_retrieves_authentication():

    retriever = Retriever()

    results = retriever.search(
        "How does authentication work?"
    )

    assert len(results) > 0

    assert results[0]["source"] == "authentication.md"


def test_deployment_query_retrieves_deployment():

    retriever = Retriever()

    results = retriever.search(
        "How should high-risk changes be deployed?"
    )

    assert len(results) > 0

    sources = [
        result["source"]
        for result in results
    ]

    assert "deployment.md" in sources