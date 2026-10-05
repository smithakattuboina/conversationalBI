from ollama import chat


def get_ai_response(user_message: str):

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response["message"]["content"]