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
            if (chip.color == ChipColor.BLACK and self._turn or
                    chip.color == ChipColor.WHITE and not self._turn):  # {
                raise ValueError("Invalid turn")
            # }
            for it in self._field[newCords[0]]:  # {
                if (it.color != chip.color):  # {
                    raise ValueError("Invalid turn")
                # }
            # }
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
                self._field[oldCords[0]].pop(oldCords[1])
                if not (
                        chip.color == ChipColor.WHITE and oldCords[0] >= 12 > newCords[0] or
                        chip.color == ChipColor.BLACK and newCords[0] >= 12 > oldCords[0]
                ):  # {
                    self._field[newCords[0]].append(chip)
                    self._field[newCords[0]][-1].inAction = False
                # }
                return result
            # }
            raise ValueError("Length mismatch")
        # }
        raise ValueError("Invalid data about old cords")
    # }
# }
