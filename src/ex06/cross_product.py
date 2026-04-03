from __future__ import annotations
from src.ex04.norm import Vector
from typing import TypeVar

T = TypeVar("T", float, int)


def cross_product(u: Vector[T], v: Vector[T]) -> Vector[T]:
    if (len(u.items) != 3 or len(v.items) != 3):
        return None

    for i in range(0, 3):
        if not (isinstance(u.items[i], float | int) and isinstance(v.items[i], float | int)):
            return None

    p1 = (u.items[1] * v.items[2]) - (u.items[2] * v.items[1])
    p2 = (u.items[2] * v.items[0]) - (u.items[0] * v.items[2])
    p3 = (u.items[0] * v.items[1]) - (u.items[1] * v.items[0])

    return [p1, p2, p3]
