import requests
import env

api_key = env.OPENROUTER_API_KEY

message = []

while True:
    prompt = input("user: ")

    if prompt.lower() == "quit":
        break

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization", f"Bearer: {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": ""
        }

    )