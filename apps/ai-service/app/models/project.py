from pydantic import BaseModel, Field


class Project(BaseModel):
    name: str = Field(default="")
    tech_stack: list[str] = Field(default_factory=list)
    github_url: str = Field(default="")
    live_url: str = Field(default="")
    description: list[str] = Field(default_factory=list)