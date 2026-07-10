from app.models.experience import Experience
from app.parsers.base_parser import BaseParser
from app.prompts.experience_prompt import EXPERIENCE_PROMPT


class ExperienceParser(BaseParser):

    def parse(
        self,
        experiences: list[str],
    ) -> list[Experience]:

        prompt = EXPERIENCE_PROMPT.format(
            experience=experiences,
        )

        return super().parse(
            prompt=prompt,
            schema=list[Experience],
        )