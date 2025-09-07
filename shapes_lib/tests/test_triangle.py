import math
import pytest
from shapes_lib import Triangle, compute_area, ValidationError, is_right_triangle

def test_triangle_area_heron_345():
    assert compute_area(Triangle(3, 4, 5)) == 6.0

def test_triangle_area_symmetry():
    assert compute_area(Triangle(5, 4, 3)) == 6.0

@pytest.mark.parametrize("sides", [
    (1, 2, 3),
    (10, 1, 1),
    (2, 2, 4),
])
def test_triangle_inequality_violations(sides):
    with pytest.raises(ValidationError):
        compute_area(Triangle(*sides))

@pytest.mark.parametrize("bad", [0, -0.1, float("inf"), float("nan")])
def test_triangle_non_positive_raises(bad):
    with pytest.raises(ValidationError):
        compute_area(Triangle(bad, 2, 3))

def test_triangle_from_dict_ok():
    assert compute_area({"type": "triangle", "a": 7, "b": 8, "c": 9}) == pytest.approx(
        26.8328, rel=0, abs=1e-4
    )

def test_triangle_from_dict_missing_key():
    with pytest.raises(KeyError):
        compute_area({"type": "triangle", "a": 3, "b": 4})
