import os
import shutil
import tempfile

from fastapi import UploadFile

from app.services.pdf_service import PDFService


class ResumeParserService:

    def __init__(self):
        self.pdf_service = PDFService()

    async def parse(self, file: UploadFile):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp:

            shutil.copyfileobj(file.file, temp)
            temp.flush()

            temp_path = temp.name

        try:
            text = self.pdf_service.extract_text(temp_path)

            return {
                "filename": file.filename,
                "text": text,
            }

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)