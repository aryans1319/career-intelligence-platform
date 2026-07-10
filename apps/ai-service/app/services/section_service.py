from app.models.section import ResumeSections
from app.services.llm_service import LLMService


class SectionService:

    def __init__(self):
        self.llm = LLMService()

    def split(self, resume_text: str) -> ResumeSections:

        prompt = f"""
You are an expert ATS resume parser.

Your job is ONLY to split the resume into sections.

IMPORTANT RULES:

1. DO NOT rewrite any text.
2. DO NOT summarize.
3. DO NOT improve grammar.
4. DO NOT remove bullet points.
5. Preserve every newline exactly as it appears.
6. Preserve spacing as much as possible.
7. Do NOT merge multiple lines into one line.
8. If a section is missing, return an empty string.
9. Return ONLY the requested schema.

Resume:

------------------------
{resume_text}
------------------------
"""

        return self.llm.generate(
            prompt,
            schema=ResumeSections
        )