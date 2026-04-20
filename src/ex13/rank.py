from __future__ import annotations
from src.ex12.inverse import Matrix as BaseMatrix
from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):
    def rank(self) -> int:
        if not self.vectors:
            return 0

        reduced = self.row_echelon()
        if reduced is None:
            return 0

        eps = 1e-12
        rank = 0

        for row in reduced.vectors:
            if any(abs(value) > eps for value in row.items):
                rank += 1

        return rank
