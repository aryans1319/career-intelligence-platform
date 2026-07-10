import os
import shutil
import tempfile

from fastapi import UploadFile

from app.services.pdf_service import PDFService
from app.services.section_service import SectionService


class ResumeParserService:

    def __init__(self):
        self.pdf_service = PDFService()
        self.section_service = SectionService()

    async def parse(self, file: UploadFile):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf",
        ) as temp:

            shutil.copyfileobj(file.file, temp)
            temp.flush()

            temp_path = temp.name

        try:

            text = self.pdf_service.extract_text(temp_path)

            sections = self.section_service.split(text)

            return {
                "filename": file.filename,
                "raw_text": text,
                "sections": sections,
            }

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)