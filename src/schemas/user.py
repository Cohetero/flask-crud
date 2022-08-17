from pydantic import BaseModel
from typing import Optional

class Users(BaseModel):
    id: Optional[int]
    name: str
    email: str
    foto: Optional[str]