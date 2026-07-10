from fastapi import APIRouter

from app.parsers.experience_parser import ExperienceParser
from app.parsers.section_parser import SectionParser
from app.services.llm_service import LLMService

router = APIRouter(
    prefix="/test",
    tags=["Test"],
)

llm = LLMService()

section_parser = SectionParser()
experience_parser = ExperienceParser()


@router.get("/experience")
def test_experience():

    text = """
Software Engineer
June 2024 – Present
Tata Consultancy Services
Kolkata, India

• Engineered scalable backend microservices using Java and Spring Boot.

• Implemented Kafka event driven workflows.

Backend Engineer
Jan 2023 – May 2024
Click.pe
Bangalore, India

• Built REST APIs in Go.
"""

    sections = section_parser.parse(text)

    experiences = experience_parser.parse(
        sections.experience
    )

    return experiences