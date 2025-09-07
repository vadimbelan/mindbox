from __future__ import annotations
from typing import Protocol, runtime_checkable, Dict, Any
import math


class ValidationError(ValueError):
    """Ошибка валидации входных данных."""


class UnknownShapeError(KeyError):
    """Запрошен неизвестный (незарегистрированный) тип фигуры."""


@runtime_checkable
class Shape(Protocol):
    def area(self) -> float: ...


@runtime_checkable
class ShapeSpec(Protocol):
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Shape": ...


def _require_positive_finite(name: str, value: float) -> None:
    if not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise ValidationError(f"{name} must be positive finite number")


def _validate_triangle_sides(a: float, b: float, c: float) -> None:
    _require_positive_finite("a", a)
    _require_positive_finite("b", b)
    _require_positive_finite("c", c)
    x, y, z = sorted((a, b, c))
    if x + y <= z:
        raise ValidationError(f"triangle inequality violated: {x} + {y} <= {z}")
