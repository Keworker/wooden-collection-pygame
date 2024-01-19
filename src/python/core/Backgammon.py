from abc import ABC as ABSTRACT, abstractmethod as abstract
from copy import deepcopy
from typing import NoReturn as Unit

from pygame import Rect

from src.python.core.Chip import Chip, ChipColor
from src.python.core.Dice import Dice


class Backgammon(ABSTRACT):  # {
    def __init__(self):  # {
        self._field: list[list[Chip]] = [[] for _ in range(0, 24, +1)]
        for i in range(0, 15, +1):  # {
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
        pass
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
    
    @abstract
    def getWinner(self) -> bool:  # {
        """
        Returns true, if white player won, false, if black player won, 
        and None, if game is still running. 
        :return: bool (nullable)
        """
        pass
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
        self._planeAssociation = list()
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
# }
