import logging

from fieldclass.config import ModelProfile
from fieldclass.experiments import get_experiment
from fieldclass.grading import grade
from fieldclass.llm import LLMOutputError, generate_structured
from fieldclass.prompts import build_feedback_messages
from fieldclass.safety import find_problems, has_digits
from fieldclass.schemas import Feedback, FeedbackText, Report

logger = logging.getLogger(__name__)

MAX_CONTENT_TRIES = 3


def evaluate_report(report: Report, profile: ModelProfile | None = None, reveal: bool = False) -> Feedback:
    experiment = get_experiment(report.topic)
    result = grade(report, experiment)
    messages = build_feedback_messages(report, experiment, result)
    problems: list[str] = []
    for attempt in range(MAX_CONTENT_TRIES):
        written = generate_structured(messages, FeedbackText, profile)
        texts = [written.went_well, written.hint, written.next_challenge]
        problems = find_problems(texts, experiment.avoid_words)
        if any(has_digits(text) for text in texts):
            problems.append("numbers in feedback")
        if not problems:
            return Feedback(
                verdict=result.verdict,
                went_well=written.went_well,
                hint=written.hint,
                next_challenge=written.next_challenge,
                mistakes=list(result.mistakes),
                problems=list(result.problems),
                concept=experiment.concept,
                expected=result.expected if reveal else None,
            )
        logger.warning("Feedback attempt %s rejected, found: %s", attempt + 1, problems)
    raise LLMOutputError(f"No acceptable feedback after {MAX_CONTENT_TRIES} tries. Last problems: {problems}")