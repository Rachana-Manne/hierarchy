"""Minimal shape hierarchy demonstrating runtime polymorphism."""

import math
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    """Abstract base class defining the common interface for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        raise NotImplementedError

    def describe(self) -> str:
        """Return the class name and area (two decimal places)."""
        return f"{self.__class__.__name__} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def render_shapes(shapes: List[Shape]) -> List[str]:
    """Call describe() on each shape without knowing its concrete type."""
    return [shape.describe() for shape in shapes]


if __name__ == "__main__":
    shapes: List[Shape] = [
        Circle(3),
        Rectangle(4, 5),
        Triangle(6, 2.5),
    ]

    for line in render_shapes(shapes):
        print(line)