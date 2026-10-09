import math 
from dataclasses import dataclass
from fieldclass.schemas import Topic 

@dataclass(frozen = True)
class ReportField:
    name:str
    label:str
    unit:str
    min_value:float
    max_value:float

@dataclass(frozen=True)
class Experiment:
    topic: Topic
    title: str
    card:str
    report_fields :tuple[ReportField, ...]

def trig_height(distance_m: float, angle_deg:float, eye_height_m:float) -> float:
    return distance_m * math.tan(math.radians(angle_deg)) + eye_height_m