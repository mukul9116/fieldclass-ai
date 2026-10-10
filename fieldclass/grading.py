from fieldclass.experiments import trig_height
from fieldclass.schemas import Topic


def expected_answer(topic: Topic, values: dict[str, float]) -> float:
    if topic == "trig_height":
        return trig_height(values["distance"], values["angle"], values["eye_height"])
    if topic == "average_velocity":
        mean_time = (values["time_1"] + values["time_2"] + values["time_3"]) / 3
        return values["distance"] / mean_time
    if topic == "statistics_counts":
        return values["most_common"] / values["total"]
    if topic == "plant_leaves":
        return values["leaf_a_length"] / values["leaf_a_width"]
    raise ValueError(f"Unknown topic: {topic}")