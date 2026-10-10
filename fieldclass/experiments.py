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
    materials: tuple[str, ...]
    steps: tuple[str, ...]
    report_fields :tuple[ReportField, ...]
    concept: str
    safety: str

def trig_height(distance_m: float, angle_deg:float, eye_height_m:float) -> float:
    return distance_m * math.tan(math.radians(angle_deg)) + eye_height_m

TRIG_HEIGHT = Experiment(
    topic="trig_height",
    title="Estimate the height of a tree or pole",
    card=(
        "Stand on flat, open ground, far from any road. "
        "Move until you must tilt your head up about 30 to 60 degrees to see the top. "
        "Measure your distance from the base with a tape or by counting steps. "
        "Make a clinometer: tape a straw along the flat edge of a protractor and hang a weighted string from its center. "
        "First sight the horizon through the straw and note where the string crosses the scale. "
        "Then sight the top and note the new reading. The angle is the difference between the two readings. "
        "Measure your eye height. "
        "Height = distance x tan(angle) + eye height."
    ),
    materials=(
        "Tape measure (or count your steps)",
        "Protractor",
        "Drinking straw",
        "String",
        "Small weight (a washer or a stone)",
        "Sticky tape",
        "Pencil and paper",
    ),
    steps=(
        "Find flat, open ground well away from roads, with a clear view of the top of a tree or pole.",
        "Build a clinometer: tape a straw along the flat edge of a protractor, and hang a weighted string from the center of the protractor.",
        "Look at the horizon through the straw and note the number where the string crosses the scale.",
        "Walk to a spot where you must tilt your head up about 30 to 60 degrees to see the top.",
        "Measure the distance from your feet to the base of the tree, with a tape or by counting steps.",
        "Look at the top through the straw and note the new number where the string crosses the scale. The angle is the difference between the two numbers.",
        "Measure the height of your eyes above the ground, then write all three measurements on paper.",
    ),
    concept=(
        "The distance and the height above your eyes form a right triangle, "
        "so tan(angle) = height above your eyes / distance, "
        "and adding your eye height gives the full height of the tree."
    ),
    report_fields=(
        ReportField("distance", "Distance from the tree", "m", 1, 100),
        ReportField("angle", "Angle up to the top", "degrees", 5, 85),
        ReportField("eye_height", "Height of your eyes", "m", 0.5, 2.2),
    ),
    safety=(
        "Stay on flat, open ground well away from roads, water and power lines. "
        "Never look at the sun through the straw. "
        "Do not climb the tree or pole, and stay off private property."
    ),
)

def record_items(experiment: Experiment) -> list[str]:
    return [f"{field.label} ({field.unit})" for field in experiment.report_fields]

EXPERIMENTS = {
    "trig_height": TRIG_HEIGHT,
}


def get_experiment(topic: str) -> Experiment:
    if topic not in EXPERIMENTS:
        available = ", ".join(EXPERIMENTS)
        raise ValueError(f"No experiment card for '{topic}' yet. Available: {available}")
    return EXPERIMENTS[topic]