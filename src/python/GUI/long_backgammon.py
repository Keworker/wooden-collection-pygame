from enum import Enum

import pygame as PyGame

from src.python.GUI.enums import BackgammonActions, GameStatus
from src.python.core.DAO import DAO
from src.python.core.LongBackgammon import LongBackgammon


def handleLongBackgammonAction(
        action: BackgammonActions,
        gameData: list,
        drawable,
        eventPos: tuple[float, float],
        eventType: Enum
) -> tuple:  # {
    """
    Handles user action at the long backgammon game.
    :param action: Type of action (maybe incorrect, autofix)
    :param gameData: List with additional game data
    :param drawable: Object, that caused collision
    :param eventPos: X and Y position of event.
    :param eventType: PyGame type of Event
    :return: Returns tuple of game status and game data
    """
    match action:  # {
        case BackgammonActions.HOLD_CHIP:  # {
            field: LongBackgammon = gameData[0]
            field.makeActive(drawable.getData()[0])
            return GameStatus.LONG_BACKGAMMON, gameData + [eventPos]
        # }
        case BackgammonActions.MOVE_CHIP:  # {
            if (eventType == PyGame.MOUSEBUTTONUP):  # {
                return handleLongBackgammonAction(
                    BackgammonActions.DROP_CHIP, gameData, drawable, eventPos, eventType
                )
            # }
            return GameStatus.LONG_BACKGAMMON, gameData[:-1] + [eventPos]
        # }
        case BackgammonActions.DROP_CHIP:  # {
            field: LongBackgammon = gameData[0]
            # noinspection PyTypeChecker
            oldPos: tuple[int, int] = None
            fieldArr = field.getField()
            for i, position in enumerate(fieldArr):  # {
                for j, chip in enumerate(position):  # {
                    if (chip.inAction):  # {
                        oldPos = (i, j)
                        break
                    # }
                # }
            # }
            try:  # {
                ind: int = field.getCollideIndex(eventPos)
            # }
            except ValueError:  # {
                ind: int = oldPos[0] if oldPos is not None else 0
            # }
            try:  # {
                if (gameData[2] is None):  # {
                    raise ValueError()
                # }
                gameData[2] = (field.makeMove(
                    fieldArr[oldPos[0]][oldPos[1]],
                    oldPos,
                    (ind, -1),
                    gameData[2][0]
                ), (gameData[2][1][0], gameData[2][1][1]))
                winner: bool = field.getWinner()
                if (winner is not None):  # {
                    gameData[2][1][0].kill()
                    gameData[2][1][1].kill()
                    DAO().addLongBackgammonGame(winner)
                    result = GameStatus.STATISTICS, []
                # }
                else:  # {
                    result = GameStatus.LONG_BACKGAMMON, gameData[:-1]
                # }
            # }
            except ValueError:  # {
                if (oldPos is not None):  # {
                    field.makePassive(oldPos)
                # }
                result = GameStatus.LONG_BACKGAMMON, gameData[:-1]
            # }
            return result
        # }
        case BackgammonActions.EXIT:  # {
            gameData[2][1][0].kill()
            gameData[2][1][1].kill()
            return GameStatus.START_SCREEN, []
        # }
    # }
    return GameStatus.LONG_BACKGAMMON, gameData
# }
