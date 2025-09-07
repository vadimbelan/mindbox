from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any
# from .core import Shape, ShapeSpec
from .core import Shape, ShapeSpec

@dataclass(frozen=True)
class Circle:
    radius: float

    def area(self) -> float:
        raise NotImplementedError("ok")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Circle":
        raise NotImplementedError("ok")
