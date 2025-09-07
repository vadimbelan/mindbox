from __future__ import annotations
from typing import Protocol, runtime_checkable, Dict, Any

class ValidationError(ValueError):

class UnknownShapeError(KeyError):

@runtime_checkable
class Shape(Protocol):
    def area(self) -> float:
        raise NotImplementedError

@runtime_checkable
class ShapeSpec(Protocol):
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Shape":
        raise NotImplementedError
