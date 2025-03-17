from pydantic import BaseModel
from typing import Optional


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    Okay: bool = True
    task_id: int
