from __future__ import annotations
from src.ex10.row_echelon import Matrix as BaseMatrix
from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):
    def determinant(self) -> float | None:
        if not self.vectors:
            return None

        size = len(self.vectors)
        if size != len(self.vectors[0].items):
            return None
        if size > 4:
            return None

        matrix = [list(row.items) for row in self.vectors]
        eps = 1e-12
        swaps = 0

        for col in range(size):
            pivot_row = col
            while pivot_row < size and abs(matrix[pivot_row][col]) <= eps:
                pivot_row += 1

            if pivot_row == size:
                return 0.0

            if pivot_row != col:
                matrix[col], matrix[pivot_row] = matrix[pivot_row], matrix[col]
                swaps += 1

            pivot = matrix[col][col]
            for row in range(col + 1, size):
                factor = matrix[row][col] / pivot
                if abs(factor) <= eps:
                    continue

                matrix[row][col] = 0.0
                for j in range(col + 1, size):
                    matrix[row][j] -= factor * matrix[col][j]

        determinant = -1.0 if swaps % 2 else 1.0
        for i in range(size):
            determinant *= matrix[i][i]

        if abs(determinant) <= eps:
            return 0.0
        return determinant
