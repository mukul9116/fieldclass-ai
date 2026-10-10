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
    avoid_words: tuple[str, ...]

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
    avoid_words=("sun", "shadow"),
)

STATISTICS_COUNTS = Experiment(
    topic="statistics_counts",
    title="Count and classify objects to find frequencies",
    card=(
        "Pick open ground such as a park, yard or school field, far from roads and water. "
        "Mark a 1 m by 1 m square on the ground with string or four stones. "
        "Choose one kind of thing to count inside it, such as fallen leaves, pebbles or flowers, "
        "and decide on up to four types, for example by color. "
        "Count how many of each type are in the square, and the total. "
        "Relative frequency of a type = its count / the total count."
    ),
    materials=(
        "String or four stones to mark the square",
        "Tape measure or a 1 m stick",
        "Pencil and paper",
    ),
    steps=(
        "Find open, safe ground such as a park, yard or school field, well away from roads and water.",
        "Mark a 1 m by 1 m square on the ground with string, sticks or four stones.",
        "Choose one kind of thing to count, such as fallen leaves, pebbles or flowers, and decide on up to four types, for example by color.",
        "Count how many items of each type are inside the square, and write each count in a small table.",
        "Add up the counts to get the total, and note the count of the most common type.",
        "If you have time, repeat in a second square at a different spot and compare the two.",
    ),
    concept=(
        "The relative frequency of a type is its count divided by the total count, "
        "and a sample from a small area lets you estimate how common each type is in the larger place."
    ),
    safety=(
        "Stay on open ground away from roads and water. "
        "Count with your eyes and do not touch unknown plants, mushrooms or insects. "
        "Do not pick or damage living plants, and wash your hands afterwards."
    ),
    report_fields=(
        ReportField("total", "Total items counted", "items", 5, 500),
        ReportField("most_common", "Count of the most common type", "items", 1, 500),
        ReportField("types", "Number of different types", "types", 1, 4),
    ),
    avoid_words=("vehicle", "cars"),
)

PLANT_LEAVES = Experiment(
    topic="plant_leaves",
    title="Observe and compare leaves",
    card=(
        "Find two different kinds of plants in a garden, park or school ground. "
        "Pick up one fallen leaf of each from the ground and do not pull leaves off living plants. "
        "Lay each leaf flat on paper and measure its length from stem to tip and its greatest width with a ruler. "
        "Count the lobes or points along the edge, and note whether the veins run in parallel lines or branch like a net. "
        "Length-to-width ratio = length / width."
    ),
    materials=(
        "Ruler",
        "Pencil and paper",
        "A flat book to press the leaves",
    ),
    steps=(
        "Find a garden, park or school ground with at least two different kinds of plants, and stay on public ground.",
        "Pick up one fallen leaf from the ground under each kind of plant. Do not pull leaves off living plants.",
        "Lay each leaf flat on paper and label them A and B.",
        "Measure each leaf's length from where the stem joins to the tip, in centimeters.",
        "Measure each leaf's greatest width, at a right angle to the length.",
        "Look at the edge of each leaf: count the lobes or points, and note whether the edge is smooth or toothed.",
        "Look at the veins: note whether they run in parallel lines or branch like a net, and write all your measurements down.",
    ),
    concept=(
        "The length-to-width ratio turns the shape of a leaf into one number, "
        "so you can compare leaves from different plants, and vein patterns often differ between plant groups."
    ),
    safety=(
        "Use only leaves that have already fallen to the ground, and do not enter private gardens. "
        "Do not touch plants you cannot name, since some irritate the skin, and never taste a leaf. "
        "Wash your hands afterwards."
    ),
    report_fields=(
        ReportField("leaf_a_length", "Length of leaf A", "cm", 0.5, 60),
        ReportField("leaf_a_width", "Width of leaf A", "cm", 0.2, 40),
        ReportField("leaf_b_length", "Length of leaf B", "cm", 0.5, 60),
        ReportField("leaf_b_width", "Width of leaf B", "cm", 0.2, 40),
    ),
    avoid_words=("taste", "eat"),
)

AVERAGE_VELOCITY = Experiment(
    topic="average_velocity",
    title="Time a moving object over a measured distance",
    card=(
        "Choose a straight, flat, car-free path such as a park path or school ground. "
        "Measure 20 m along it with a tape and mark the start and finish. "
        "A friend walks from the start to the finish at a steady pace while you time them with a stopwatch. "
        "Repeat three times and write each time in seconds. "
        "Average velocity = distance / time."
    ),
    materials=(
        "Tape measure",
        "Stopwatch (a watch or the stopwatch on a phone)",
        "Two markers such as stones or chalk",
        "A friend to walk",
        "Pencil and paper",
    ),
    steps=(
        "Find a straight, flat, car-free path, such as a park path or a school ground.",
        "Measure 20 m along the path with a tape and mark the start and the finish.",
        "Ask your friend to stand at the start line, and stand beside the finish line with the stopwatch.",
        "Say 'go' and start the stopwatch at the same moment your friend starts walking at a steady pace.",
        "Stop the stopwatch when your friend crosses the finish line and write down the time in seconds.",
        "Repeat for three runs, and write each time on paper.",
    ),
    concept=(
        "Average velocity is the distance covered along a straight line divided by the time taken, "
        "and repeating the measurement shows how much real timings vary."
    ),
    safety=(
        "Use a flat, car-free path, never a road or a parking area. "
        "Walk at a steady pace and do not run on uneven or wet ground. "
        "Keep the path clear of other people while you time."
    ),
    report_fields=(
        ReportField("distance", "Distance of the path", "m", 5, 100),
        ReportField("time_1", "Time of run 1", "s", 1, 120),
        ReportField("time_2", "Time of run 2", "s", 1, 120),
        ReportField("time_3", "Time of run 3", "s", 1, 120),
    ),
    avoid_words=("sprint", "cycl", "bike", "skate"),
)

EXPERIMENTS = {
    "trig_height": TRIG_HEIGHT,
    "statistics_counts": STATISTICS_COUNTS,
    "plant_leaves": PLANT_LEAVES,
    "average_velocity": AVERAGE_VELOCITY,
}

def record_items(experiment: Experiment) -> list[str]:
    return [f"{field.label} ({field.unit})" for field in experiment.report_fields]


def get_experiment(topic: str) -> Experiment:
    if topic not in EXPERIMENTS:
        available = ", ".join(EXPERIMENTS)
        raise ValueError(f"No experiment card for '{topic}' yet. Available: {available}")
    return EXPERIMENTS[topic]