from __future__ import annotations
from src.ex08.trace import Matrix as BaseMatrix

from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):
    def transpose(self) -> Matrix[T] | None:
        if not self.vectors:
            return None
        return Matrix([list(row) for row in zip(*self.vectors)])
