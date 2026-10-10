import pytest

from fieldclass.experiments import TRIG_HEIGHT
from fieldclass.grading import expected_answer, grade
from fieldclass.schemas import Report

def test_trig_expected():
    values = {"distance": 10, "angle": 45, "eye_height": 1.5}
    assert expected_answer("trig_height", values) == pytest.approx(11.5)


def test_velocity_expected():
    values = {"distance": 20, "time_1": 10, "time_2": 20, "time_3": 15}
    assert expected_answer("average_velocity", values) == pytest.approx(20 / 15)

def test_statistics_expected():
    values = {"total": 40, "most_common": 10, "types": 3}
    assert expected_answer("statistics_counts", values) == pytest.approx(0.25)


def test_leaves_expected():
    values = {"leaf_a_length": 8, "leaf_a_width": 4, "leaf_b_length": 6, "leaf_b_width": 3}
    assert expected_answer("plant_leaves", values) == pytest.approx(2.0)

GOOD_VALUES = {"distance": 10, "angle": 45, "eye_height": 1.5}


def make_report(answer, values=GOOD_VALUES):
    return Report(topic="trig_height", values=values, answer=answer)


def test_correct_answer():
    assert grade(make_report(11.5), TRIG_HEIGHT).verdict == "correct"


def test_partial_answer():
    assert grade(make_report(13.0), TRIG_HEIGHT).verdict == "partial"


def test_incorrect_answer():
    assert grade(make_report(5.0), TRIG_HEIGHT).verdict == "incorrect"


def test_missing_answer():
    assert grade(make_report(None), TRIG_HEIGHT).verdict == "missing_info"