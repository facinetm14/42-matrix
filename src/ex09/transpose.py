from __future__ import annotations
from src.ex08.trace import Matrix as BaseMatrix
from src.ex00 import Vector

from typing import TypeVar

T = TypeVar("T", float, int)


class Matrix(BaseMatrix):
    def transpose(self) -> T:
        return Matrix([list(row) for row in zip(*self.vectors)])
