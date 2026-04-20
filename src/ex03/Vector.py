from __future__ import annotations
from src.ex00.Vector import Vector as BaseVector
from typing import TypeVar

T = TypeVar("T", int, float)

class Vector(BaseVector):
  def dot(self, other: Vector[T]) -> T | None:
    len_items = len(self.items)
    if  len_items == 0 or len_items != len(other.items):
      return None
    dot_product = self.items[0] * other.items[0]

    if len_items == 1:
      return dot_product
    
    for i in range(1, len_items):
      dot_product += self.items[i] * other.items[i]

    return dot_product

