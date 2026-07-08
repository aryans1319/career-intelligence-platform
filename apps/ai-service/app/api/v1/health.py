from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "ai-service",
        "version": "0.1.0"
    }