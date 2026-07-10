from pydantic import BaseModel, Field


class Job(BaseModel):
    title: str

    company: str

    location: str | None = None

    summary: str = ""

    responsibilities: list[str] = Field(default_factory=list)

    required_skills: list[str] = Field(default_factory=list)

    preferred_skills: list[str] = Field(default_factory=list)