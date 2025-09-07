from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any
import math
from .core import Shape, ShapeSpec, _validate_triangle_sides


@dataclass(frozen=True)
class Triangle:
    a: float
    b: float
    c: float

    def area(self) -> float:
        _validate_triangle_sides(self.a, self.b, self.c)
        p = (self.a + self.b + self.c) / 2.0
        under = max(p * (p - self.a) * (p - self.b) * (p - self.c), 0.0)
        return math.sqrt(under)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Triangle":
        try:
            a = float(data["a"])
            b = float(data["b"])
            c = float(data["c"])
        except KeyError as e:
            raise KeyError(f"missing key: {e.args[0]}") from e
        _validate_triangle_sides(a, b, c)
        return cls(a, b, c)
