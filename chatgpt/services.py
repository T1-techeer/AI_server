from chatgpt.schemas import RefactorRequest
from openai import OpenAI
import openai
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

client = openai.OpenAI(api_key=api_key)

def gpt_prompt(request: RefactorRequest) -> str:
    # Prompt 구성
    prompt = f"Please {request.type} this code to improve its structure, readability, or performance."
    return prompt

def chat(code: str, type: str) -> str:
    # RefactorRequest 객체 생성
    request = RefactorRequest(previousCode=code, type=type)

    # gpt_prompt 함수를 사용하여 프롬프트 생성
    prompt = gpt_prompt(request)

    # OpenAI GPT-3.5 모델을 사용하여 API 호출
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": code},
    ],
    max_tokens=500,
    temperature=0.9)
    return response.choices[0].message.content

