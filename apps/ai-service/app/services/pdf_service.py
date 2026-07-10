import fitz


class PDFService:

    def extract_text(self, pdf_path: str) -> str:
        document = fitz.open(pdf_path)

        try:
            page_texts = []

            for page in document:

                blocks = page.get_text("blocks")

                blocks.sort(key=lambda block: (block[1], block[0]))

                text = "\n\n".join(
                    block[4].strip()
                    for block in blocks
                    if block[4].strip()
                )

                page_texts.append(text)

            return "\n\n".join(page_texts)

        finally:
            document.close()