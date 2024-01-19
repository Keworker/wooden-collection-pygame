from src.python.core.Backgammon import Backgammon, getNewLength
from src.python.core.Chip import Chip
from src.python.core.Dice import Dice


class LongBackgammon(Backgammon):  # {
    # @Override
    def _makeMoveExtended(
            self, chip: Chip, oldCords: tuple[int, int],
            newCords: tuple[int, int], length: tuple[Dice, Dice]
    ) -> tuple[Dice, Dice]:  # {
        if (self._field[oldCords[0]][oldCords[1]] == chip):  # {
            self._checkColorsNormal(chip.color, self._turn, newCords[0])
            deltaCords: int = newCords[0] - oldCords[0] if (
                    newCords[0] > oldCords[0]) else \
                len(self._field) + newCords[0] - oldCords[0]
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
