from .core import Shape, ValidationError, UnknownShapeError
from .circle import Circle
from .triangle import Triangle
from .registry import register_shape

from typing import Protocol, Union, Dict, Any

def compute_area(shape_or_spec: "Shape | dict") -> float:
    raise NotImplementedError("ok")

def is_right_triangle(a: float, b: float, c: float, *, eps: float = 1e-9) -> bool:
    raise NotImplementedError("ok")

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
