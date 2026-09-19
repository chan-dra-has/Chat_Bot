import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key
)


messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    }
]


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages
    )

    answer = response.choices[0].message.content

    print("AI:", answer)

    messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )