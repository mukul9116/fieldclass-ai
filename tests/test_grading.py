import pytest

from fieldclass.grading import expected_answer


def test_trig_expected():
    values = {"distance": 10, "angle": 45, "eye_height": 1.5}
    assert expected_answer("trig_height", values) == pytest.approx(11.5)


def test_velocity_expected():
    values = {"distance": 20, "time_1": 10, "time_2": 20, "time_3": 15}
    assert expected_answer("average_velocity", values) == pytest.approx(20 / 15)