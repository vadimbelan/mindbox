import math
import pytest
from shapes_lib import Circle, compute_area, ValidationError

def test_circle_area_basic():
    assert compute_area(Circle(1)) == math.pi

def test_circle_area_float_and_precision():
    assert compute_area(Circle(2.5)) == math.pi * 2.5**2

@pytest.mark.parametrize("bad", [0, -1, float("inf"), float("nan")])
def test_circle_bad_radius_raises(bad):
    with pytest.raises(ValidationError):
        compute_area(Circle(bad))

def test_circle_from_dict_ok():
    assert compute_area({"type": "circle", "radius": 3}) == math.pi * 9

def test_circle_from_dict_alt_key_r():
    assert compute_area({"type": "circle", "r": 2}) == math.pi * 4
