from pydantic import BaseModel, Field


class Education(BaseModel):
    institution: str = Field(default="")
    degree: str = Field(default="")
    field_of_study: str = Field(default="")
    start_date: str = Field(default="")
    end_date: str = Field(default="")
    cgpa: str = Field(default="")