from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    completed: bool = False
    due_date: Optional[str] = None