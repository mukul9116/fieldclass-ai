import pytest
from pydantic import ValidationError

from fieldclass.schemas import MissionRequest


def test_request_defaults():
    request = MissionRequest(topic="trig_height")
    assert request.difficulty == "medium"
    assert request.minutes == 30


def test_request_rejects_unknown_topic():
    with pytest.raises(ValidationError):
        MissionRequest(topic="cooking")


def test_request_rejects_too_many_minutes():
    with pytest.raises(ValidationError):
        MissionRequest(topic="trig_height", minutes=500)