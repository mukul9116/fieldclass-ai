from dataclasses import dataclass
from typing import Literal
import math

from fieldclass.experiments import Experiment, trig_height
from fieldclass.schemas import Report, Topic

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

Verdict = Literal["correct", "partial", "incorrect", "missing_info"]

CORRECT_TOLERANCE = 0.05
PARTIAL_TOLERANCE = 0.25


@dataclass(frozen=True)
class Grade:
    verdict: Verdict
    expected: float | None = None
    problems: tuple[str, ...] = ()
    mistakes: tuple[str, ...] = ()


def check_values(report: Report, experiment: Experiment) -> list[str]:
    problems = []
    for field in experiment.report_fields:
        value = report.values.get(field.name)
        if value is None:
            problems.append(f"{field.label} is missing")
        elif not field.min_value <= value <= field.max_value:
            problems.append(
                f"{field.label} should be between {field.min_value} and {field.max_value} {field.unit}"
            )
    if report.answer is None:
        problems.append("Your calculated answer is missing")
    return problems

def likely_mistakes(topic: Topic, values: dict[str, float]) -> dict[str, float]:
    if topic == "trig_height":
        d, a, e = values["distance"], values["angle"], values["eye_height"]
        return {
            "you may have forgotten to add your eye height": d * math.tan(math.radians(a)),
            "your calculator may be in radian mode instead of degree mode": d * math.tan(a) + e,
            "you may have used sine instead of tangent": d * math.sin(math.radians(a)) + e,
            "you may have used cosine instead of tangent": d * math.cos(math.radians(a)) + e,
        }
    if topic == "average_velocity":
        mean_time = (values["time_1"] + values["time_2"] + values["time_3"]) / 3
        return {
            "you may have divided time by distance instead of distance by time": mean_time / values["distance"],
            "you may have used only one of the three times": values["distance"] / values["time_1"],
        }
    if topic == "statistics_counts":
        return {
            "you may have given a percentage; here we want a fraction such as 0.25": 100 * values["most_common"] / values["total"],
        }
    if topic == "plant_leaves":
        return {
            "you may have divided width by length instead of length by width": values["leaf_a_width"] / values["leaf_a_length"],
        }
    return {}

def diagnose(report: Report) -> list[str]:
    found = []
    for message, wrong in likely_mistakes(report.topic, report.values).items():
        if wrong != 0 and abs(report.answer - wrong) / abs(wrong) <= CORRECT_TOLERANCE:
            found.append(message)
    return found

def grade(report: Report, experiment: Experiment) -> Grade:
    problems = check_values(report, experiment)
    if problems:
        return Grade("missing_info", None, tuple(problems))
    expected = expected_answer(report.topic, report.values)
    error = abs(report.answer - expected) / expected
    if error <= CORRECT_TOLERANCE:
        verdict = "correct"
    elif error <= PARTIAL_TOLERANCE:
        verdict = "partial"
    else:
        verdict = "incorrect"

    mistakes = [] if verdict == "correct" else diagnose(report)
    return Grade(verdict, expected, mistakes=tuple(mistakes))