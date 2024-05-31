from fastapi import APIRouter, HTTPException
from chatgpt.schemas import RefactorRequest
from chatgpt.services import chat
from chatgpt.services import makeImage

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
async def image_api(keyword: str):
    try:
        # service 코드
        customized_image_url = makeImage(keyword)
        return {"customized_image_url": customized_image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))