from __future__ import annotations
from typing import Any, Dict

from .core import Shape, ValidationError, UnknownShapeError
from .circle import Circle
from .triangle import Triangle
from .registry import register_shape as _register_shape_impl, from_spec as _from_spec


def register_shape(name: str, from_dict_callable):
    return _register_shape_impl(name, from_dict_callable)


_register_shape_impl("circle", Circle.from_dict)
_register_shape_impl("triangle", Triangle.from_dict)


def compute_area(shape_or_spec: "Shape | Dict[str, Any]") -> float:
    if isinstance(shape_or_spec, dict):
        shape = _from_spec(shape_or_spec)
        return shape.area()
    if not hasattr(shape_or_spec, "area"):
        raise ValidationError("object must implement .area() or pass a dict spec")
    return float(shape_or_spec.area())


def is_right_triangle(a: float, b: float, c: float, *, eps: float = 1e-9) -> bool:
    from .core import _validate_triangle_sides

    _validate_triangle_sides(a, b, c)
    x, y, z = sorted((float(a), float(b), float(c)))
    lhs = x * x + y * y
    rhs = z * z
    return abs(lhs - rhs) <= eps * max(rhs, 1.0)


__all__ = [
    "Shape",
    "ValidationError",
    "UnknownShapeError",
    "Circle",
    "Triangle",
    "register_shape",
    "compute_area",
    "is_right_triangle",
]
