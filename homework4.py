import requests

API_KEY = "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"

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

prompts = [
    "Explain artificial intelligence in one sentence.",
    "Explain artificial intelligence in detail with examples.",
    "Explain artificial intelligence like I am a beginner."
]

for i, prompt in enumerate(prompts, start=1):
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    print(f"\n===== Test {i} =====")
    print("Prompt:", prompt)

    try:
        print("Response:", result["choices"][0]["message"]["content"])
    except:
        print("Error:", result)