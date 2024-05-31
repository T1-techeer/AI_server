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

def makeImage(keyword: str) -> str:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"Create a minimalist homepage for {keyword} with a clean design. The page should feature a large banner showcasing a few high-quality grocery products like snacks and beverages, neatly arranged with adequate white space and margins. Use a soft, pastel color palette with a light blue background to create a fresh look. The navigation bar at the top should include simple categories such as 'Home', 'Shop', 'Deals', and 'Contact'. Include a centered search bar and icons for login and shopping cart aligned to the right. Below the banner, display a section for featured deals with only a few product images and brief descriptions, ensuring elements are evenly spaced and not too close to the edges. Maintain a clean, balanced, and easy-to-navigate layout. Do not include any images of monitors or screens.",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url

