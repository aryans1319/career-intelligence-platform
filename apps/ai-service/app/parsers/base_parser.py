from typing import Any

from app.services.llm_service import LLMService


class BaseParser:

    def __init__(self):
        self.llm = LLMService()

    def parse(
        self,
        prompt: str,
        schema: Any,
    ):
        return self.llm.generate(
            prompt=prompt,
            schema=schema,
        )