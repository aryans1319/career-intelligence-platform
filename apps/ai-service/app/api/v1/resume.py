from fastapi import APIRouter, File, UploadFile

from app.services.resume_parser_service import ResumeParserService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)

parser_service = ResumeParserService()


@router.post("/parse")
async def parse_resume(
    file: UploadFile = File(...)
):
    return await parser_service.parse(file)