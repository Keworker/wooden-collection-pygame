from src.python.core.Backgammon import Backgammon
from src.python.core.Chip import Chip, ChipColor
from src.python.core.ConstantDice import ConstantDice
from src.python.core.Dice import Dice


class LongBackgammon(Backgammon):  # {
    def __init__(self):  # {
        super().__init__()
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
            deltaCords: int = newCords[0] - oldCords[0] if (
                    newCords[0] > oldCords[0]) else \
                len(self._field) + newCords[0] - oldCords[0]
            result = None
            if (length[0].getValue() == deltaCords):  # {
                result = (ConstantDice(0), length[1])
            # }
            if (length[1].getValue() == deltaCords):  # {
                result = (length[0], ConstantDice(0))
            # }
            if (length[0].getValue() + length[1].getValue() == deltaCords):  # {
                result = (ConstantDice(0), ConstantDice(0))
            # }
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

    # @Override
    def getWinner(self) -> bool:  # {
        hasBlack: bool = False
        hasWhite: bool = False
        for position in self._field:  # {
            for chip in position:  # {
                hasBlack |= (chip.color == ChipColor.BLACK)
                hasWhite |= (chip.color == ChipColor.WHITE)
            # }
        # }
        if (hasBlack and not hasWhite):  # {
            return True
        # }
        if (hasWhite and not hasBlack):  # {
            return False
        # }
        # noinspection PyTypeChecker
        return None
    # }
# }
