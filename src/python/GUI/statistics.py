import pygame as PyGame
from pygame import Surface, Rect
from pygame.draw import rect as drawRect

from src.python.GUI.colors import BLACK, RED, GREEN
from src.python.GUI.enums import StatisticsActions
from src.python.GUI.strings import TOTAL_GAMES_TXT, LONG_BACKGAMMON_GAMES_TXT, SHORT_BACKGAMMON_GAMES_TXT, \
    SHORT_BACKGAMMON_GAMES_BLACK_WON_TXT, SHORT_BACKGAMMON_GAMES_WHITE_WON_TXT, LONG_BACKGAMMON_GAMES_BLACK_WON_TXT, \
    LONG_BACKGAMMON_GAMES_WHITE_WON_TXT
from src.python.core.DAO import DAO
from src.python.utils.resources_handler import getFont


def drawStatistics(surface: Surface) -> list:  # {
    """
    Drawing games statistics at given surface and return list of clickable objects.
    :param surface: Surface for drawing statistics
    :return: Clickable objects list
    """
    surface.fill(BLACK)
    screenSize: tuple = surface.get_size()
    exitButtonSize: float = screenSize[1] / 15
    rect: Rect = Rect(
        screenSize[0] - exitButtonSize * 2,
        screenSize[1] - exitButtonSize * 2,
        exitButtonSize,
        exitButtonSize
    )
    drawRect(surface, RED, rect, border_radius=int(exitButtonSize / 6))
    clickable: list = [(rect, StatisticsActions.EXIT)]
    font: PyGame.font = PyGame.font.Font(getFont(), screenSize[1] // 24)
    _, fontHeight = font.size("A")
    offset: int = (screenSize[1] // 12 - fontHeight) // 2
    dao: DAO = DAO()
    longBackgammonGames: int = dao.getLongBackgammonGamesCount()
    shortBackgammonGames: int = dao.getShortBackgammonGamesCount()
    totalGames: int = longBackgammonGames + shortBackgammonGames
    longBackgammonWhiteWon: int = dao.getLongBackgammonGamesCount(True)
    longBackgammonBlackWon: int = dao.getLongBackgammonGamesCount(False)
    shortBackgammonWhiteWon: int = dao.getShortBackgammonGamesCount(True)
    shortBackgammonBlackWon: int = dao.getShortBackgammonGamesCount(False)
    surface.blit(
        font.render(
            TOTAL_GAMES_TXT.format(totalGames),
            False,
            GREEN
        ),
        (offset, offset)
    )
    surface.blit(
        font.render(
            LONG_BACKGAMMON_GAMES_TXT.format(longBackgammonGames),
            False,
            GREEN
        ),
        (offset, offset * 2 + fontHeight)
    )
    surface.blit(
        font.render(
            SHORT_BACKGAMMON_GAMES_TXT.format(shortBackgammonGames),
            False,
            GREEN
        ),
        (offset, offset * 3 + fontHeight * 2)
    )
    surface.blit(
        font.render(
            LONG_BACKGAMMON_GAMES_WHITE_WON_TXT.format(longBackgammonWhiteWon),
            False,
            GREEN
        ),
        (offset, offset * 4 + fontHeight * 3)
    )
    surface.blit(
        font.render(
            LONG_BACKGAMMON_GAMES_BLACK_WON_TXT.format(longBackgammonBlackWon),
            False,
            GREEN
        ),
        (offset, offset * 5 + fontHeight * 4)
    )
    surface.blit(
        font.render(
            SHORT_BACKGAMMON_GAMES_WHITE_WON_TXT.format(shortBackgammonWhiteWon),
            False,
            GREEN
        ),
        (offset, offset * 6 + fontHeight * 5)
    )
    surface.blit(
        font.render(
            SHORT_BACKGAMMON_GAMES_BLACK_WON_TXT.format(shortBackgammonBlackWon),
            False,
            GREEN
        ),
        (offset, offset * 7 + fontHeight * 6)
    )
    return clickable
# }

