from pydantic import BaseModel, Field

class PersonalInfo(BaseModel):
    full_name: str = Field(default="")
    email: str = Field(default="")
    phone: str = Field(default="")
    linkedin: str = Field(default="")
    github: str = Field(default="")
    portfolio: str = Field(default="")
    location: str = Field(default="")