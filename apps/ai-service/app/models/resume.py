from pydantic import BaseModel, Field

from app.models.certification import Certification
from app.models.education import Education
from app.models.experience import Experience
from app.models.personal_info import PersonalInfo
from app.models.project import Project
from app.models.skill import Skills


class Resume(BaseModel):
    personal_info: PersonalInfo

    summary: str = ""

    experience: list[Experience] = Field(default_factory=list)

    projects: list[Project] = Field(default_factory=list)

    skills: Skills = Field(default_factory=Skills)

    education: list[Education] = Field(default_factory=list)

    certifications: list[Certification] = Field(default_factory=list)

    achievements: list[str] = Field(default_factory=list)