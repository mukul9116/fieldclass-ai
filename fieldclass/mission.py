import logging

from fieldclass.config import ModelProfile
from fieldclass.experiments import get_experiment, record_items
from fieldclass.llm import LLMOutputError, generate_structured
from fieldclass.prompts import build_mission_messages
from fieldclass.safety import find_problems
from fieldclass.schemas import FieldMission, Mission, MissionRequest

logger = logging.getLogger(__name__)

MAX_CONTENT_TRIES = 3


def generate_mission(request: MissionRequest, profile: ModelProfile | None = None) -> Mission:
    experiment = get_experiment(request.topic)
    messages = build_mission_messages(request, experiment)
    problems: list[str] = []
    for attempt in range(MAX_CONTENT_TRIES):
        written = generate_structured(messages, FieldMission, profile)
        problems = find_problems(
            [written.title, written.objective, written.tip], experiment.avoid_words
        )
        if not problems:
            return Mission(
                topic=request.topic,
                difficulty=request.difficulty,
                minutes=request.minutes,
                title=written.title,
                objective=written.objective,
                tip=written.tip,
                materials=list(experiment.materials),
                steps=list(experiment.steps),
                record=record_items(experiment),
                concept=experiment.concept,
                safety=experiment.safety,
            )
        logger.warning("Attempt %s rejected, found: %s", attempt + 1, problems)
    raise LLMOutputError(f"No acceptable mission after {MAX_CONTENT_TRIES} tries. Last problems: {problems}")