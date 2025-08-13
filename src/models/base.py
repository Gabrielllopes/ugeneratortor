from pydantic import BaseModel
from enum import StrEnum

class Language(StrEnum):
  ENGLISH = "English"
  SPANISH = "Spanish"
  PORTUGUESE = "Portuguese"
  FRENCH = "French"

class Carrossel(BaseModel):
  title: str
  slide: list[str]
  legend: str