"""
Write a program to determine whether a triangle is equilateral, isosceles, or
scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has exactly two sides of the same length.

A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0,
and the sum of the lengths of any two sides must be greater than the length
of the third side.
"""


class Triangle:
    def __init__(self, side_1: int, side_2: int, side_3: int):
        self.sides = (side_1, side_2, side_3)
        if not self.is_valid_triangle():
            raise ValueError("Triangle is invalid.")

    def is_valid_triangle(self) -> bool:
        for i, _ in enumerate(self.sides):
            if self.sides[i] <= 0 or \
               self.sides[i] >= self.sides[(i+1) % 3] + self.sides[(i+2) % 3]:
                return False
        return True

    @property
    def kind(self) -> str:
        num_distinct_sides = len(set(self.sides))
        match num_distinct_sides:
            case 1:
                triangle_type = "equilateral"
            case 2:
                triangle_type = "isosceles"
            case 3:
                triangle_type = "scalene"
        return triangle_type
