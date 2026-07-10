from datetime import date

from pydantic import BaseModel


class Education(BaseModel):
    institution: str

    degree: str

    branch: str | None = None

    cgpa: float | None = None

    start_date: date | None = None

    end_date: date | None = None