from datetime import date

from pydantic import BaseModel


class Certification(BaseModel):
    name: str

    issuer: str | None = None

    issue_date: date | None = None