from __future__ import annotations
from typing import TypeVar, Generic


T = TypeVar("T", int, float)

class Vector (Generic[T]):
  
  def __init__(self, items: list[T]):
    self.items = items
  
  def __repr__(self):
    return f"{self.items}"
  
  def __iter__(self):
    return iter(self.items)
  
  def __add__(self, other):
    return self.add(other)

  def __mul__(self, scalar: T):
    return self.scl(scalar)
  
  def add(self, v: Vector[T]) -> Vector[T]:
    if len(v.items) != len(self.items):
      raise ArithmeticError("You can't add 2 vectors with differents size")
    return Vector[T]([self.items[i] + v.items[i] for i in range(0, len(self.items))])
  
  def sub(self, v: Vector[T]) -> Vector[T]:
    if len(v.items) != len(self.items):
      raise ArithmeticError("You can't sub 2 vectors with differents size")
    return Vector[T]([self.items[i] - v.items[i] for i in range(0, len(self.items))])
  
  def scl(self, k: T):
    return Vector[T]([item * k for item in self.items])

