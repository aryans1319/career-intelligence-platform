from pydantic import BaseModel, EmailStr, HttpUrl

class PersonalInfo(BaseModel):
    full_name: str
    email: EmailStr | None = None
    phone: str | None = None
    location: str | None = None

    linkedin: HttpUrl | None = None
    github: HttpUrl | None = None
    portfolio: HttpUrl | None = None