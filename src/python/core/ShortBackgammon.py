from src.python.core.Backgammon import Backgammon, getNewLength
from src.python.core.Chip import ChipColor, Chip
from src.python.core.Dice import Dice


class ShortBackgammon(Backgammon):  # {
    def __init__(self):  # {
        super().__init__()
        self._field[0] = [Chip(ChipColor.BLACK) for _ in range(2)]
        self._field[11] = [Chip(ChipColor.BLACK) for _ in range(5)]
        self._field[16] = [Chip(ChipColor.BLACK) for _ in range(3)]
        self._field[18] = [Chip(ChipColor.BLACK) for _ in range(5)]
        self._field[5] = [Chip(ChipColor.WHITE) for _ in range(5)]
        self._field[7] = [Chip(ChipColor.WHITE) for _ in range(3)]
        self._field[12] = [Chip(ChipColor.WHITE) for _ in range(5)]
        self._field[23] = [Chip(ChipColor.WHITE) for _ in range(2)]
    # }

    # @Override
    def _makeMoveExtended(
            self, chip: Chip, oldCords: tuple[int, int],
            newCords: tuple[int, int], length: tuple[Dice, Dice]
    ) -> tuple[Dice, Dice]:  # {
        if (self._field[oldCords[0]][oldCords[1]] == chip):  # {
            self._checkColorsNormal(chip.color, self._turn, newCords[0])
            if (chip.color == ChipColor.WHITE):  # {
                deltaCords: int = newCords[0] - oldCords[0] if (
                        newCords[0] > oldCords[0]) else \
                    len(self._field) + newCords[0] - oldCords[0]
            # }
            else:  # {
                deltaCords: int = newCords[0] - 23 - oldCords[0] if (
                        newCords[0] > oldCords[0]) else \
                    oldCords[0] - newCords[0]
            # }
            result = getNewLength(length, deltaCords)
            if (result is not None):  # {
                self._makeMove(oldCords, newCords, chip)
                return result
            # }
            raise ValueError("Length mismatch")
        # }
        raise ValueError("Invalid data about old cords")
    # }
# }
