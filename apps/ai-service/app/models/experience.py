from datetime import date

from pydantic import BaseModel, Field


class Experience(BaseModel):
    company: str
    role: str

    start_date: date | None = None
    end_date: date | None = None

    location: str | None = None

    description: list[str] = Field(default_factory=list)

    tech_stack: list[str] = Field(default_factory=list)