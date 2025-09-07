from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any
from .core import Shape, ShapeSpec

@dataclass(frozen=True)
class Triangle:
    a: float
    b: float
    c: float

    def area(self) -> float:
        raise NotImplementedError("ok")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Triangle":
        raise NotImplementedError("ok")
