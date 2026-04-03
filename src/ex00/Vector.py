from __future__ import annotations
from typing import TypeVar, Generic


T = TypeVar("T", int, float)


class Vector(Generic[T]):

    def __init__(self, items: list[T]):
        self.items = items

    def __repr__(self):
        return f"{self.items}"

    def __iter__(self):
        return iter(self.items)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, scalar: T):
        return self.scl(scalar)

    def add(self, v: Vector[T]) -> Vector[T] | None:
        if len(v.items) != len(self.items):
            return None

        items: list[T] = []

        for i in range(0, len(self.items)):
            if not (
                isinstance(self.items[i], float | int)
                and isinstance(v.items[i], float | int)
            ):
                return None

            items.append(self.items[i] + v.items[i])

        return Vector(items)

    def sub(self, v: Vector[T]) -> Vector[T] | None:
        if len(v.items) != len(self.items):
            return None

        items: list[T] = []

        for i in range(0, len(self.items)):
            if not (
                isinstance(self.items[i], float | int)
                and isinstance(v.items[i], float | int)
            ):
                return None

            items.append(self.items[i] - v.items[i])

        return Vector(items)

    def scl(self, k: T):
        if not isinstance(k, float | int):
            return None

        items: list[T] = []

        for i in range(0, len(self.items)):
            if not isinstance(self.items[i], float | int):
                return None

            items.append(self.items[i] * k)

        return Vector(items)
