import pytest
from shapes_lib import (
    compute_area,
    register_shape,
    ValidationError,
    UnknownShapeError,
)

def test_compute_area_from_dict_requires_type_key():
    with pytest.raises(ValidationError):
        compute_area({})

def test_compute_area_from_dict_unknown_type():
    with pytest.raises(UnknownShapeError):
        compute_area({"type": "hexagon", "side": 3})

def test_compute_area_with_wrong_object():
    class NoArea:
        pass
    with pytest.raises(ValidationError):
        compute_area(NoArea())

def test_spec_must_be_dict():
    with pytest.raises(ValidationError):
        # type: ignore[arg-type]
        compute_area("not a dict")

def test_register_new_shape_and_use():
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
        def area(self):
            if not (isinstance(self.width, (int, float)) and isinstance(self.height, (int, float))):
                raise AssertionError("test-only guard")
            if self.width <= 0 or self.height <= 0:
                from shapes_lib import ValidationError
                raise ValidationError("width/height must be positive finite number")
            return float(self.width) * float(self.height)
        @classmethod
        def from_dict(cls, d):
            return cls(d["width"], d["height"])

    register_shape("rectangle", Rectangle.from_dict)
    assert compute_area({"type": "rectangle", "width": 3, "height": 5}) == 15.0
