from pydantic import BaseModel
class RefactorRequest(BaseModel):
    previousCode: str
    type: str