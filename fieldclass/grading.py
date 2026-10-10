from dataclasses import dataclass
from typing import Literal

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
    return Grade(verdict, expected)