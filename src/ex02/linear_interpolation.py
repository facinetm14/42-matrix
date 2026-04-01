from __future__ import annotations
from typing import TypeVar
from src.ex00.Vector import Vector


T = TypeVar("T")
U = TypeVar("U", int, float)


def lerp(u: T, v: T, t: U) -> T:
    return (u * (1 - t)) + (v * t)
