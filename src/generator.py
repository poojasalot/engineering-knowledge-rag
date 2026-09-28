import ollama


def generate_answer(question: str, results: list[dict]) -> str:
    if not results:
        return (
            "I don't have enough information in the engineering "
            "documentation to answer this."
        )
    context_parts = []

    for result in results:
        context_parts.append(
            f"""
SOURCE: {result['source']}
CHUNK: {result['chunk_id']}

{result['content']}
"""
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an engineering knowledge assistant.

Answer the user's question using ONLY the engineering
documentation provided below.

Do not invent information.

If the documentation does not contain enough information,
say:

"I don't have enough information in the engineering
documentation to answer this."

When making a recommendation, mention the relevant
source document in parentheses.

Engineering documentation:

{context}

User question:

{question}

Provide a concise, practical answer.
"""

    response = ollama.chat(
        model="qwen-claude:latest",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response["message"]["content"]