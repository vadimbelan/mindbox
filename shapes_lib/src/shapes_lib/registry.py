from __future__ import annotations
from typing import Callable, Dict, Any
from .core import Shape, UnknownShapeError, ValidationError

_REGISTRY: Dict[str, Callable[[Dict[str, Any]], Shape]] = {}


def register_shape(name: str, from_dict: Callable[[Dict[str, Any]], Shape]) -> None:
    if not isinstance(name, str) or not name:
        raise ValidationError("shape name must be non-empty string")
    _REGISTRY[name.lower()] = from_dict


def from_spec(spec: Dict[str, Any]) -> Shape:
    if not isinstance(spec, dict):
        raise ValidationError("spec must be a dict")
    if "type" not in spec:
        raise ValidationError("spec must include 'type'")
    type_name = str(spec["type"]).lower()
    try:
        factory = _REGISTRY[type_name]
    except KeyError as e:
        raise UnknownShapeError(f"unknown shape type: {type_name}") from e
    return factory(spec)
