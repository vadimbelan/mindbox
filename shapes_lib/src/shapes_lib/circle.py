from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any
import math
from .core import _require_positive_finite


@dataclass(frozen=True)
class Circle:
    radius: float

    def area(self) -> float:
        _require_positive_finite("radius", self.radius)
        return math.pi * (self.radius**2)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Circle":
        r = data.get("radius", data.get("r", None))
        _require_positive_finite("radius", r)
        return cls(float(r))
