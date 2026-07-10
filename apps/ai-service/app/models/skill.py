from pydantic import BaseModel, Field


class Skills(BaseModel):
    languages: list[str] = Field(default_factory=list)

    frameworks: list[str] = Field(default_factory=list)

    databases: list[str] = Field(default_factory=list)

    cloud: list[str] = Field(default_factory=list)

    devops: list[str] = Field(default_factory=list)

    ai: list[str] = Field(default_factory=list)

    tools: list[str] = Field(default_factory=list)

    concepts: list[str] = Field(default_factory=list)