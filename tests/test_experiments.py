import pytest 
from fieldclass.experiments import trig_height, TRIG_HEIGHT, record_items

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