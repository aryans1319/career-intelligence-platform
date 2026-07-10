from app.models.section import ResumeSections
from app.parsers.base_parser import BaseParser
from app.prompts.section_prompt import SECTION_PROMPT


class SectionParser(BaseParser):

    def parse(
        self,
        resume_text: str,
    ) -> ResumeSections:

        prompt = SECTION_PROMPT.format(
            resume=resume_text,
        )

        return super().parse(
            prompt=prompt,
            schema=ResumeSections,
        )