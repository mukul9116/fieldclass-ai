import pytest 
from fieldclass.experiments import trig_height

def test_trig_height_at_45_degrees():
    assert trig_height(10, 45, 1.5) == pytest.approx(11.5)

def test_trig_height_at_zero_angle_is_eye_height():
    assert trig_height(10, 0, 1.5) == pytest.approx(1.5)

def test_trig_height_at_30_degrees():
    assert trig_height(10, 30, 1.5) == pytest.approx(7.27, abs=0.01)