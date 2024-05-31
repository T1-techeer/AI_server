from openai import OpenAI

client = OpenAI()
def chat(message: str) -> str:
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are a friendly and casual assistant. Please respond informally in Korean."},
        {"role": "user", "content": message},
    ],
    max_tokens=500,
    temperature=0.9)
    return response.choices[0].message.content