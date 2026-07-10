from pydantic import BaseModel, Field

from app.models.personal_info import PersonalInfo
from app.models.experience import Experience
from app.models.project import Project
from app.models.skill import Skills
from app.models.education import Education


class Resume(BaseModel):
    personal_info: PersonalInfo = Field(default_factory=PersonalInfo)

    summary: str = Field(default="")

    experiences: list[Experience] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    skills: Skills = Field(default_factory=Skills)

    education: list[Education] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)

    achievements: list[str] = Field(default_factory=list)