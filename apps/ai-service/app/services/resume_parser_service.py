from fastapi import UploadFile


class ResumeParserService:

    async def parse(
        self,
        file: UploadFile,
    ):
        return {
            "filename": file.filename,
            "status": "parser not implemented",
        }