from __future__ import annotations
from src.ex09.transpose import Matrix as BaseMatrix
from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):
    def row_echelon(self) -> Matrix[T] | None:
        if not self.vectors:
            return None

        rows = len(self.vectors)
        cols = len(self.vectors[0].items)
        matrix = [list(row.items) for row in self.vectors]
        lead = 0
        eps = 1e-12

        for r in range(rows):
            while lead < cols and all(abs(matrix[i][lead]) <= eps for i in range(r, rows)):
                lead += 1

            if lead == cols:
                break

            pivot_row = r
            while pivot_row < rows and abs(matrix[pivot_row][lead]) <= eps:
                pivot_row += 1

            if pivot_row == rows:
                lead += 1
                if lead == cols:
                    break
                continue

            if pivot_row != r:
                matrix[r], matrix[pivot_row] = matrix[pivot_row], matrix[r]

            pivot = matrix[r][lead]
            matrix[r] = [value / pivot for value in matrix[r]]

            for i in range(rows):
                if i == r:
                    continue
                factor = matrix[i][lead]
                if abs(factor) <= eps:
                    continue
                matrix[i] = [
                    matrix[i][j] - factor * matrix[r][j]
                    for j in range(cols)
                ]

            lead += 1
            if lead == cols:
                break

        for i in range(rows):
            matrix[i] = [0.0 if abs(
                value) <= eps else value for value in matrix[i]]

        return Matrix(matrix)
