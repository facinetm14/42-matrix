from __future__ import annotations
from typing import TypeVar, Generic
from src.ex00.Vector import Vector


T = TypeVar("T", int, float)


class Matrix(Generic[T]):

    def __init__(self, vectors: list[Vector[T]] | list[list[T]]):
        matrix_vectors: list[Vector[T]] = []

        if isinstance(vectors[0], Vector):
            matrix_vectors.append(vectors[0])
            vector_len = len(vectors[0].items)

            for i in range(1, len(vectors)):
                if len(vectors[i].items) != vector_len:
                    raise ValueError(
                        "Invalid Matrix: vectors should have the same size"
                    )
                matrix_vectors.append(vectors[i])

        else:
            matrix_vectors.append(Vector(vectors[0]))
            vector_len = len(vectors[0])

            for i in range(1, len(vectors)):
                if len(vectors[i]) != vector_len:
                    raise ValueError(
                        "Invalid Matrix: vectors should have the same size"
                    )
                matrix_vectors.append(Vector(vectors[i]))

        self.vectors = matrix_vectors

    def __repr__(self):
        return f"{self.vectors}"

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, scalar: T):
        return self.scl(scalar)

    def add(self, m: Matrix[T]) -> Matrix[T]:
        if len(m.vectors) != len(self.vectors):
            return None
        matrix_vectors: list[Vector[T]] = []

        for i in range(0, len(self.vectors)):
            sum_vec = self.vectors[i].add(m.vectors[i])
            if sum_vec == None:
                return None
            matrix_vectors.append(sum_vec)
        return Matrix(matrix_vectors)

    def sub(self, m: Matrix[T]) -> Matrix[T]:
        if len(m.vectors) != len(self.vectors):
            return None
        matrix_vectors: list[Vector[T]] = []

        for i in range(0, len(self.vectors)):
            sub_vec = self.vectors[i].sub(m.vectors[i])
            if sub_vec == None:
                return None
            matrix_vectors.append(sub_vec)
        return Matrix(matrix_vectors)

    def scl(self, k: T):
        matrix_vectors: list[Vector[T]] = []

        for i in range(0, len(self.vectors)):
            sub_vec = self.vectors[i].scl(k)
            if sub_vec == None:
                return None
            matrix_vectors.append(sub_vec)
        return Matrix(matrix_vectors)
