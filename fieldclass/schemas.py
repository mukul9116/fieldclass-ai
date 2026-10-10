from typing import Literal
from pydantic import BaseModel, Field

Topic = Literal["trig_height", "statistics_counts", 'plant_leaves', 'average_velocity']
Difficulty = Literal['easy', 'medium', 'hard']

class MissionRequest(BaseModel):
    topic: Topic
    difficulty: Difficulty = "medium"
    minutes: int = Field(default=30, ge=10, le=120)
    notes: str | None = Field(default =None, max_length = 500)

class FieldMission(BaseModel):
    title : str = Field(max_length = 60)
    objective: str = Field(max_length = 240)
    materials: list[str] = Field(min_length = 1, max_length = 5)
    steps: list[str] = Field(min_length=2, max_length=8)
    record: list[str] = Field(min_length = 1, max_length=6)
    safety: str = Field(max_length = 160)
    concept: str = Field(max_length=400)
