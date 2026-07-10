from pydantic import BaseModel, Field


class MatchResult(BaseModel):
    score: float = 0.0

    matched_skills: list[str] = Field(default_factory=list)

    missing_skills: list[str] = Field(default_factory=list)

    suggestions: list[str] = Field(default_factory=list)