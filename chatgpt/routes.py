
from fastapi import APIRouter


router = APIRouter(prefix='api/v1/chatgpt')

@router.post("/refactor")
async def chat_api():
    response = 