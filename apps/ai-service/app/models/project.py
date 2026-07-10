from pydantic import BaseModel, Field, HttpUrl


class Project(BaseModel):
    name: str

    description: list[str] = Field(default_factory=list)

    tech_stack: list[str] = Field(default_factory=list)

    github: HttpUrl | None = None

    live_url: HttpUrl | None = None