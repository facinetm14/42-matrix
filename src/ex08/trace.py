from __future__ import annotations
from src.ex07.linear_map import Matrix as BaseMatrix
from typing import TypeVar

T = TypeVar("T", float, int)

class Matrix(BaseMatrix):
  def trace(self) -> T:
    col = len(self.vectors[0].items)
    if col != len(self.vectors):
      return None
    result = 0
    for i in range(0, col):
      result += self.vectors[i].items[i]
    return result
