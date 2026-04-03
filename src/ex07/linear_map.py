from __future__ import annotations
from src.ex00.Matrix import Matrix as BaseMatrix
from src.ex03.Vector import Vector
from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):

    def __init__(self, vectors: list[Vector[T]] | list[list[T]]):
        matrix_vectors: list[Vector[T]] = []

        if isinstance(vectors[0], Vector):
            matrix_vectors.append(vectors[0])
            vector_len = len(vectors[0].items)

            for i in range(1, len(vectors)):
                if len(vectors[i].items) != vector_len:
                    raise ValueError(
                        "Invalid Martrix: vectors should have the same size"
                    )
                matrix_vectors.append(vectors[i])
        else:
            matrix_vectors.append(Vector(vectors[0]))
            vector_len = len(vectors[0])

            for i in range(1, len(vectors)):
                if len(vectors[i]) != vector_len:
                    raise ValueError(
                        "Invalid Martrix: vectors should have the same size"
                    )
                matrix_vectors.append(Vector(vectors[i]))

        self.vectors = matrix_vectors

    def mul_vec(self, vector: Vector[T]) -> Vector[T] | None:
        vector_len = len(vector.items)

        if vector_len != len(self.vectors[0].items):
            return None

        result = []
        for i in range(0, len(vector.items)):
            result.append(self.vectors[i].dot(vector))
        return Vector(result)

    def mul_mat(self, matrix: Matrix[T]) -> Matrix[T] | None:
        if len(matrix.vectors) != len(self.vectors[0].items):
            return None
        transposed_matrix = [Vector(list(row)) for row in zip(*matrix.vectors)]
        result_matrix = []

        for v in self.vectors:
            row_i = [v.dot(t) for t in transposed_matrix]
            result_matrix.append(row_i)
        return Matrix(result_matrix)
