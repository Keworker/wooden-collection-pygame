from enum import Enum


class ChipColor(Enum):  # {
    BLACK = 0
    WHITE = 1
# }


class Chip:  # {
    def __init__(self, color: ChipColor):  # {
        self.color: ChipColor = color
        self.inAction: bool = False
    # }

    def __eq__(self, other):  # {
        return self.color == other.color and self.inAction == other.inAction
    # }
# }
