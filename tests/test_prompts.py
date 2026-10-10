from fieldclass.experiments import TRIG_HEIGHT
from fieldclass.prompts import build_mission_messages
from fieldclass.schemas import MissionRequest

def test_messages_have_system_and_user():

    request = MissionRequest(topic="trig_height")
    messages = build_mission_messages(request, TRIG_HEIGHT)

    assert len(messages) == 2
    assert messages[0]["role"] == "system"
    assert TRIG_HEIGHT.card in messages[1]["content"]

def test_notes_only_appear_when_given():

    with_notes = build_mission_messages(
        MissionRequest(topic="trig_height", notes="I have a garden"), TRIG_HEIGHT
    )
    without_notes = build_mission_messages(
        MissionRequest(topic="trig_height"), TRIG_HEIGHT
    )

    assert "I have a garden" in with_notes[1]["content"]
    assert "I have a garden" not in without_notes[1]["content"]