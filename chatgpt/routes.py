from fastapi import APIRouter, HTTPException
from chatgpt.schemas import RefactorRequest
from chatgpt.services import chat

router = APIRouter(prefix='/api/v1/chatgpt')

from pydantic import BaseModel

@router.post("/refactor")
async def chat_api(request: RefactorRequest):
    try:
        # service 코드
        refactored_code = chat(request.previousCode, request.type)
        return {"refactored_code": refactored_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/image")
async def chat_api():

    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt="Create a minimalist homepage for an online grocery store with a clean design. The page should feature a large banner showcasing a few high-quality grocery products like snacks and beverages, neatly arranged with adequate white space and margins. Use a soft, pastel color palette with a light blue background to create a fresh look. The navigation bar at the top should include simple categories such as 'Home', 'Shop', 'Deals', and 'Contact'. Include a centered search bar and icons for login and shopping cart aligned to the right. Below the banner, display a section for featured deals with only a few product images and brief descriptions, ensuring elements are evenly spaced and not too close to the edges. Maintain a clean, balanced, and easy-to-navigate layout. Do not include any images of monitors or screens.",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url