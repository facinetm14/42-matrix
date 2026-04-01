from __future__ import annotations
from src.ex04.norm import Vector
from typing import TypeVar

T = TypeVar("T", float, int)


def angle_cos(u: Vector[T], v: Vector[T]) -> T | None:

    if len(u.items) != len(v.items):
        return None
    norm_u = u.norm_2()
    if norm_u == 0:
        return None

    norm_v = v.norm_2()
    if norm_v == 0:
        return None
    return (u.dot(v)) / (norm_u * norm_v)
