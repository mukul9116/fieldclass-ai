from pathlib import Path

from fieldclass.experiments import Experiment
from fieldclass.grading import Grade
from fieldclass.schemas import MissionRequest, Report

PROMPTS_DIR =Path(__file__).resolve().parent.parent /  "prompts"

def load_prompt(filename: str) -> str:
    return (PROMPTS_DIR / filename).read_text(encoding="utf-8").strip()

def build_mission_messages(request:MissionRequest, experiment: Experiment) -> list[dict]:
    user_text = (
        f"Experiment: {experiment.title}\n"
        f"{experiment.card}\n\n"
        f"Student: difficulty {request.difficulty}, {request.minutes} minutes available"
    )

    if request.notes:
        user_text += f"\nNotes from the student: {request.notes}"

    return [
        {"role": "system", "content": load_prompt("mission_system.txt")},
        {"role": "user", "content": user_text},
    ]

VERDICT_WORDS = {
    "correct": "The student's calculated answer is correct.",
    "partial": "The student's answer is close but not quite right.",
    "incorrect": "The student's answer is not right.",
    "missing_info": "The student's report has missing or impossible information.",
}


def build_feedback_messages(report: Report, experiment: Experiment, grade: Grade) -> list[dict]:
    lines = [f"Experiment: {experiment.title}", VERDICT_WORDS[grade.verdict]]
    if grade.problems:
        lines.append("Problems with the report: " + "; ".join(grade.problems))
    if grade.mistakes:
        lines.append("Likely mistakes: " + "; ".join(grade.mistakes))
    if report.observations:
        lines.append(f"Student observations: {report.observations}")
    if report.reflection:
        lines.append(f"Student reflection: {report.reflection}")
    return [
        {"role": "system", "content": load_prompt("feedback_system.txt")},
        {"role": "user", "content": "\n".join(lines)},
    ]