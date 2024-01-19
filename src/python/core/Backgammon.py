from abc import ABC as ABSTRACT, abstractmethod as abstract
from copy import deepcopy
from typing import NoReturn as Unit

from pygame import Rect

from src.python.core.Chip import Chip, ChipColor
from src.python.core.ConstantDice import ConstantDice
from src.python.core.Dice import Dice


def getNewLength(length: tuple[Dice, Dice], deltaCords: int) -> tuple[Dice, Dice]:  # {
    """
    Returns new length by old length and delta cords
    :param length: old length
    :param deltaCords: int delta of cords
    :return: tuple
    """
    if (length[0].getValue() == deltaCords):  # {
        return (ConstantDice(0), length[1])
    # }
    if (length[1].getValue() == deltaCords):  # {
        return (length[0], ConstantDice(0))
    # }
    if (length[0].getValue() + length[1].getValue() == deltaCords):  # {
        return (ConstantDice(0), ConstantDice(0))
    # }
# }


class Backgammon(ABSTRACT):  # {
    def __init__(self):  # {
        self._field: list[list[Chip]] = [[] for _ in range(0, 24, +1)]
        for _ in range(0, 15, +1):  # {
            self._field[0].append(Chip(ChipColor.WHITE))
            self._field[12].append(Chip(ChipColor.BLACK))
        # }
        self._turn: bool = True
        # noinspection PyTypeChecker
        self._planeAssociation: list[tuple[Rect, int]] = None
    # }

    @abstract
    def _makeMoveExtended(
            self, chip: Chip, oldCords: tuple[int, int],
            newCords: tuple[int, int], length: tuple[Dice, Dice]
    ) -> tuple[Dice, Dice]:  # {
        """
        protected abstract method
        :param chip: Chip
        :param oldCords: tuple[int, int]
        :param newCords: tuple[int, int]
        :param length: length[Dice, Dice]
        :return: tuple[Dice, Dice]
        """
    # }

    def makeMove(
            self, chip: Chip, oldCords: tuple[int, int],
            newCords: tuple[int, int], length: tuple[Dice, Dice]
    ) -> tuple[Dice, Dice]:  # {
        """
        Checking if move is correct.
        Returns tuple of length, with deducted value by current length.
        Throws ValueError, if data is invalid, or if you try to move
        not chip of current player, or move is too short / too long.
        :param chip: A chip, which will be moved
        :param oldCords: Old cords of chip on field
        :param newCords: New cords of chip on field
        :param length: Numbers, thrown with dice (maximum length of current move)
        :return: Tuple of length, with deducted value by current length
        """
        result: tuple[Dice, Dice] = self._makeMoveExtended(chip, oldCords, newCords, length)
        if ((result[0].getValue(), result[1].getValue()) == (0, 0)):  # {
            self._turn = not self._turn
        # }
        return result
    # }

    def getWinner(self) -> bool:  # {
        """
        Returns true, if white player won, false, if black player won,
        and None, if game is still running.
        :return: bool (nullable)
        """
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

    def getTurn(self) -> bool:  # {
        """
        Get color of current player
        :return: True, if white player, False, if black player
        """
        return self._turn
    # }

    def getField(self) -> list[list[Chip]]:  # {
        """
        Returns game's field as a list. Check out docs:
        https://github.com/Keworker/wooden-collection-pygame/blob/master/docs/Backgammon%20Field.md
        :return: game's field as a list
        """
        return deepcopy(self._field)
    # }

    def makeActive(self, cords: tuple[int, int]) -> Unit:  # {
        """
        Marks given chip as "In action".
        :param cords: Cords of the unit to be activated
        :return: Unit
        """
        self._field[cords[0]][cords[1]].inAction = True
    # }

    def makePassive(self, cords: tuple[int, int]) -> Unit:  # {
        """
        Marks given chip as "Not in action".
        :param cords: Cords of the unit to be deactivated
        :return: Unit
        """
        self._field[cords[0]][cords[1]].inAction = False
    # }

    def associateWithPlane(self, width: int, height: int) -> Unit:  # {
        """
        Associate cords to field's positions.
        :param width: Width of current rect
        :param height: Height of current rect
        :return: Unit
        """
        self._planeAssociation = []
        rectWidth: float = width / 12
        rectHeight: float = height / 2
        for i in range(0, 12, +1):  # {
            self._planeAssociation.append((
                Rect(width - (i + 1) * rectWidth, -1, rectWidth, rectHeight), i
            ))
        # }
        for i in range(12, 24, +1):  # {
            self._planeAssociation.append((
                Rect((i - 12) * rectWidth, rectHeight, rectWidth, rectHeight), i
            ))
        # }
    # }

    def isAssociatedWithPlane(self) -> bool:  # {
        """
        Returns true, if field already associated with plane, else, false.
        :return: boolean value
        """
        return self._planeAssociation is not None
    # }

    def getCollideIndex(self, cords: tuple[float, float]) -> int:  # {
        """
        Returns index of field's array by cords, if field already associated with plane.
        :param cords: Cords of finding index
        :return: Integer value - index from 0 to 23
        """
        if not (self.isAssociatedWithPlane()):  # {
            raise ValueError("Field not associated with plane yet")
        # }
        for rect, i in self._planeAssociation:  # {
            if (rect.collidepoint(*cords)):  # {
                return i
            # }
        # }
        raise ValueError("Invalid cords")
    # }

    def _checkColorsNormal(self, curColor: ChipColor, turn: bool, newPosition: int) -> Unit:  # {
        if (curColor == ChipColor.BLACK and turn or
                curColor == ChipColor.WHITE and not turn):  # {
            raise ValueError("Invalid turn")
        # }
        for it in self._field[newPosition]:  # {
            if (it.color != curColor):  # {
                raise ValueError("Invalid turn")
            # }
        # }
    # }

    def _makeMove(
            self,
            oldCords: tuple[int, int],
            newCords: tuple[int, int],
            chip: Chip
    ) -> Unit:  # {
        self._field[oldCords[0]].pop(oldCords[1])
        if not (
                chip.color == ChipColor.WHITE and oldCords[0] >= 12 > newCords[0] or
                chip.color == ChipColor.BLACK and newCords[0] >= 12 > oldCords[0]
        ):  # {
            self._field[newCords[0]].append(chip)
            self._field[newCords[0]][-1].inAction = False
        # }
    # }
# }
