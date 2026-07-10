# app/models/summary.py

from pydantic import BaseModel

class Summary(BaseModel):
    content: str = ""