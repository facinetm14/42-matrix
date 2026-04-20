from __future__ import annotations
from src.ex11.determinant import Matrix as BaseMatrix
from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):
    def inverse(self) -> Matrix[T] | None:
        if not self.vectors:
            return None

        size = len(self.vectors)
        if size != len(self.vectors[0].items):
            return None

        eps = 1e-12
        augmented = []

        for i in range(size):
            row = list(self.vectors[i].items)
            identity_row = [0.0] * size
            identity_row[i] = 1.0
            augmented.append(row + identity_row)

        for col in range(size):
            pivot_row = col
            while pivot_row < size and abs(augmented[pivot_row][col]) <= eps:
                pivot_row += 1

            if pivot_row == size:
                return None

            if pivot_row != col:
                augmented[col], augmented[pivot_row] = (
                    augmented[pivot_row],
                    augmented[col],
                )

            pivot = augmented[col][col]
            for j in range(col, 2 * size):
                augmented[col][j] /= pivot

            for row in range(size):
                if row == col:
                    continue

                factor = augmented[row][col]
                if abs(factor) <= eps:
                    continue

                augmented[row][col] = 0.0
                for j in range(col + 1, 2 * size):
                    augmented[row][j] -= factor * augmented[col][j]

        inverse_matrix = []
        for i in range(size):
            inverse_row = []
            for value in augmented[i][size:]:
                inverse_row.append(0.0 if abs(value) <= eps else value)
            inverse_matrix.append(inverse_row)

        return Matrix(inverse_matrix)
