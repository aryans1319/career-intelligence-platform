from google import genai

from app.core.config import settings


class LLMService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def hello(self) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Reply with only: Hello Aryan"
        )

        return response.text