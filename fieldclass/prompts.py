from pathlib import Path
from fieldclass.experiments import Experiment
from fieldclass.schemas import MissionRequest

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