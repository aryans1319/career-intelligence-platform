from fastapi import APIRouter

from app.services.llm_service import LLMService

router = APIRouter(prefix="/test", tags=["Test"])

llm = LLMService()


@router.get("/llm")
def test_llm():
    return {
        "response": llm.hello()
    }
