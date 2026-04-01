from __future__ import annotations
from typing import TypeVar, Generic
from src.ex00.Vector import Vector


T = TypeVar("T", int, float)


class Matrix(Generic[T]):

    def __init__(self, vectors: list[Vector[T]] | list[list[T]]):
        if isinstance(vectors[0], Vector):
            self.vectors = vectors
        else:
            self.vectors = [Vector[T](v) for v in vectors]

    def __repr__(self):
        return f"{self.vectors}"

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, scalar: T):
        return self.scl(scalar)

    def add(self, m: Matrix[T]) -> Matrix[T]:
        if len(m.vectors) != len(self.vectors):
            raise ArithmeticError(
                "You can't add 2 Matrixs with differents vectors size"
            )
        return Matrix[T](
            [self.vectors[i].add(m.vectors[i]) for i in range(0, len(self.vectors))]
        )

    def sub(self, m: Matrix[T]) -> Matrix[T]:
        if len(m.vectors) != len(self.vectors):
            raise ArithmeticError(
                "You can't sub 2 Matrixs with differents vectors size"
            )
        return Matrix[T](
            [self.vectors[i].sub(m.vectors[i]) for i in range(0, len(self.vectors))]
        )

    def scl(self, k: T):
        return Vector[T]([v.scl(k) for v in self.vectors])
