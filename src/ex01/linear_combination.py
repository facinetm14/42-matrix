from __future__ import annotations
from typing import TypeVar
from src.ex00.Vector import Vector


T = TypeVar("T", int, float)


def linear_combination(vectors: list[Vector[T]], scalars: list[T]) -> Vector[T] | None:
    len_scalars = len(scalars)

    if len_scalars < 1 or len(vectors) != len_scalars:
        return None
    result = vectors[0].scl(scalars[0])

    if len_scalars == 1 or result == None:
        return result

    for i in range(1, len(scalars)):
        new_result = vectors[i].scl(scalars[i])

        if new_result == None:
            return None

        result += new_result

    return result
