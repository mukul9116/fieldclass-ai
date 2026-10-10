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
    title: str = Field(max_length=80)
    objective: str = Field(max_length=300)
    tip: str = Field(max_length=300)

class Mission(BaseModel):
    topic: Topic
    difficulty: Difficulty
    minutes: int
    title: str
    objective: str
    tip: str
    materials: list[str]
    steps: list[str]
    record: list[str]
    concept: str
    safety: str

class Report(BaseModel):
    topic: Topic
    values: dict[str, float]
    answer: float | None = None
    observations: str = Field(default="", max_length=600)
    reflection: str = Field(default="", max_length=600)

class FeedbackText(BaseModel):
    next_challenge: str = Field(max_length=300)


class Feedback(BaseModel):
    verdict: str
    went_well: str
    hint: str
    next_challenge: str
    mistakes: list[str]
    problems: list[str]
    concept: str
    expected: float | None = None