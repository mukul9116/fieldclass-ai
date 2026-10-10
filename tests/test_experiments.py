import pytest 
from fieldclass.experiments import trig_height, TRIG_HEIGHT, record_items, get_experiment, EXPERIMENTS
from typing import get_args
from fieldclass.schemas import Topic

def test_trig_height_at_45_degrees():
    assert trig_height(10, 45, 1.5) == pytest.approx(11.5)

def test_trig_height_at_zero_angle_is_eye_height():
    assert trig_height(10, 0, 1.5) == pytest.approx(1.5)

def test_trig_height_at_30_degrees():
    assert trig_height(10, 30, 1.5) == pytest.approx(7.27, abs=0.01)

def test_all_numbers_are_positive():
    for field in TRIG_HEIGHT.report_fields:
        assert field.min_value < field.max_value

def test_record_items_for_trig_height():
    items = record_items(TRIG_HEIGHT)
    assert len(items) == 3
    assert items[0] == "Distance from the tree (m)"

def test_trig_safety_mentions_roads():
    assert "road" in TRIG_HEIGHT.safety.lower()

def test_unknown_topic_gives_clear_error():
    with pytest.raises(ValueError, match="No experiment card"):
        get_experiment("cooking")

def test_trig_has_materials_and_steps():
    assert len(TRIG_HEIGHT.materials) >= 3
    assert len(TRIG_HEIGHT.steps) >= 5

def test_every_experiment_is_complete():
    for topic, experiment in EXPERIMENTS.items():
        assert experiment.topic == topic
        assert len(experiment.materials) >= 3
        assert len(experiment.steps) >= 5
        assert experiment.safety
        for field in experiment.report_fields:
            assert field.min_value < field.max_value


def test_every_topic_has_a_card():
    assert set(EXPERIMENTS) == set(get_args(Topic))