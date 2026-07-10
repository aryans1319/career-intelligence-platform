from pydantic import BaseModel, Field


class ResumeSections(BaseModel):
    personal_info: str = Field(default="")
    summary: str = Field(default="")

    experience: list[str] = Field(default_factory=list)

    projects: list[str] = Field(default_factory=list)

    skills: str = Field(default="")

    education: str = Field(default="")

    certifications: str = Field(default="")