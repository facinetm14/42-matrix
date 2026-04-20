from __future__ import annotations
from src.ex03.Vector import Vector as BaseVector
from typing import TypeVar


class Vector(BaseVector):
    def norm_1(self) -> float:
        norm = 0
        for item in self.items:
            norm += item if item >= 0 else item * (-1)
        return norm

    def norm_2(self) -> float:
        norm = 0
        for item in self.items:
            norm += pow(item, 2)
        return pow(norm, 0.5)

    def norm_inf(self) -> float:
        if len(self.items) == 0:
            return 0
        return max([item if item >= 0 else item * (-1) for item in self.items])
