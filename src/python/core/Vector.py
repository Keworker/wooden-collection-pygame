from math import hypot


class Vector:  # {
    def __init__(self, x: float, y: float):  # {
        self.x: float = x
        self.y: float = y
    # }

    def __add__(self, other):  # {
        return Vector(self.x + other.x, self.y + other.y)
    # }

    def __sub__(self, other):  # {
        return Vector(self.x - other.x, self.y - other.y)
    # }

    def __mul__(self, other):  # {
        return Vector(self.x * other, self.y * other)
    # }

    def length(self) -> float:  # {
        """
        Returns float length of the vector (abs of vector).
        :return: float number
        """
        return hypot(self.x, self.y)
    # }
# }
