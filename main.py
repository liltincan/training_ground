import requests
import env
import time

api_key = env.OPENROUTER_API_KEY

messages = []

while True:
    prompt = input("user: ")
    start = time.perf_counter()

    if prompt.lower() == "quit":
        break

    messages.append({
        "role": "user",
        "content": prompt
    })

    for attempt in range(3):
      try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "liquid/lfm-3-1.7b:free",
                "messages": messages,
                "reasoning": {"enabled": True}
            },
            timeout=60
        )

      response.raise_for_status()
      break

      data = response.json()
      assistant_message = data["choices"][0]["message"]

      messages.append(assistant_message)

      end = time.perf_counter()
      print("ChadLite:", assistant_message.get("content"))
      print(end - start)
