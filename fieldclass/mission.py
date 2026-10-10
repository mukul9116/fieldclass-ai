from fieldclass.config import ModelProfile
from fieldclass.experiments import get_experiment, record_items
from fieldclass.llm import generate_structured
from fieldclass.prompts import build_mission_messages
from fieldclass.schemas import FieldMission, Mission, MissionRequest


def generate_mission(request: MissionRequest, profile: ModelProfile | None = None) -> Mission:
    experiment = get_experiment(request.topic)
    messages = build_mission_messages(request, experiment)
    written = generate_structured(messages, FieldMission, profile)
    return Mission(
        topic=request.topic,
        difficulty=request.difficulty,
        minutes=request.minutes,
        title=written.title,
        objective=written.objective,
        materials=written.materials,
        steps=written.steps,
        record=record_items(experiment),
        concept=experiment.concept,
        safety=experiment.safety,
    )