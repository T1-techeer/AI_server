from fastapi import APIRouter, HTTPException
from chatgpt.schemas import RefactorRequest
from chatgpt.services import chat

router = APIRouter(prefix='/api/v1/chatgpt')

@router.post("/refactor")
async def chat_api(request: RefactorRequest):
    try:
        # service 코드
        refactored_code = chat(request.previousCode, request.type)
        return {"refactored_code": refactored_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))