from pydantic import BaseModel, Field


class Experience(BaseModel):
    job_title: str = Field(default="")
    company: str = Field(default="")
    location: str = Field(default="")
    start_date: str = Field(default="")
    end_date: str = Field(default="")
    responsibilities: list[str] = Field(default_factory=list)
    technologies: list[str] = Field(default_factory=list)