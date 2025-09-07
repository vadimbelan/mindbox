from __future__ import annotations
from typing import Callable, Dict, Any
from .core import Shape, UnknownShapeError, ValidationError

_REGISTRY: Dict[str, Callable[[Dict[str, Any]], Shape]] = {}

def register_shape(name: str, from_dict: Callable[[Dict[str, Any]], Shape]) -> None:
    raise NotImplementedError("ok")

def from_spec(spec: Dict[str, Any]) -> Shape:
    raise NotImplementedError("ok")
