"""Abstract shape hierarchy demonstrating abstraction and polymorphism."""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Common interface that every shape must implement."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("side lengths must be positive")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("side lengths violate the triangle inequality")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def __str__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


def total_metrics(shapes: list[Shape]) -> tuple[float, float]:
    """Return (sum of areas, sum of perimeters) for the given shapes."""
    total_area = sum(shape.area() for shape in shapes)
    total_perimeter = sum(shape.perimeter() for shape in shapes)
    return total_area, total_perimeter


if __name__ == "__main__":
    shapes: list[Shape] = [
        Circle(2.5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
    ]

    for shape in shapes:
        print(f"{shape}: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")

    total_area, total_perimeter = total_metrics(shapes)
    print(f"Total area: {total_area:.2f}")
    print(f"Total perimeter: {total_perimeter:.2f}")