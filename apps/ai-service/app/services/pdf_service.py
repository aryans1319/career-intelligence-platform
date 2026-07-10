import fitz

class PDFService:

    def extract_text(self, pdf_path: str) -> str:
        document = fitz.open(pdf_path)

        try:
            text = ""

            for page in document:
                text += page.get_text()

            return text

        finally:
            document.close()