from pydantic import BaseModel, Field
from datetime import date
from typing import Optional


class GameCreate(BaseModel):
    title: str
    release_date: date
    description: Optional[str] = None


class GameInDB(GameCreate):
    id: str = Field(..., alias="_id")
