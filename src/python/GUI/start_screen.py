from typing import NoReturn as Unit

import pygame as PyGame
from pygame import Surface, Rect
from pygame.draw import rect as drawRect

from src.python.GUI.colors import DEFAULT_COLOR, BUTTON_COLOR, TEXT_COLOR
from src.python.GUI.enums import StartScreenActions
from src.python.GUI.strings import (SHORT_BACKGAMMON_TXT,
                                    LONG_BACKGAMMON_TXT,
                                    STATISTICS_TXT,
                                    EXIT_TXT)
from src.python.utils.resources_handler import getFont


def handleStartScreenAction(action) -> Unit:  # {
    """
    Handles action that caused at the start screen.
    :param action: Action to be handled
    :return: Void (Unit (NoReturn))
    """
    match action:  # {
        case StartScreenActions.OPEN_SHORT_BACKGAMMON:  # {
            pass
        # }
        case StartScreenActions.OPEN_LONG_BACKGAMMON:  # {
            pass
        # }
        case StartScreenActions.OPEN_STATISTICS:  # {
            pass
        # }
        case StartScreenActions.EXIT:  # {
            raise KeyboardInterrupt()
        # }
    # }
# }


def drawStartScreen(surface: Surface) -> list:  # {
    """
    Draws start screen UI on given surface.
    :param surface: Surface for drawing
    :return: List of clickable objects on screen
    """
    clickable: list = []
    width, height = surface.get_size()
    font: PyGame.font = PyGame.font.Font(getFont(), height // 24)
    _, fontHeight = font.size("A")
    offset: int = (height // 12 - fontHeight) // 2
    surface.fill(DEFAULT_COLOR)
    shortBackgammonButton: Rect = Rect(
        width // 2 - width // 4,
        height - height // 24 * 12,
        width // 2,
        height // 12
    )
    clickable.append((
        shortBackgammonButton,
        StartScreenActions.OPEN_SHORT_BACKGAMMON
    ))
    drawRect(surface, BUTTON_COLOR, shortBackgammonButton, 0, shortBackgammonButton.height // 6)
    surface.blit(
        font.render(
            SHORT_BACKGAMMON_TXT,
            False,
            TEXT_COLOR
        ),
        (shortBackgammonButton.left + offset, shortBackgammonButton.top + offset)
    )
    longBackgammonButton: Rect = Rect(
        shortBackgammonButton.left,
        height - height // 24 * 9,
        shortBackgammonButton.width,
        shortBackgammonButton.height
    )
    clickable.append((
        longBackgammonButton,
        StartScreenActions.OPEN_LONG_BACKGAMMON
    ))
    drawRect(surface, BUTTON_COLOR, longBackgammonButton, 0, longBackgammonButton.height // 6)
    surface.blit(
        font.render(
            LONG_BACKGAMMON_TXT,
            False,
            TEXT_COLOR
        ),
        (longBackgammonButton.left + offset, longBackgammonButton.top + offset)
    )
    statisticsButton: Rect = Rect(
        shortBackgammonButton.left,
        height - height // 24 * 6,
        shortBackgammonButton.width,
        shortBackgammonButton.height
    )
    clickable.append((
        statisticsButton,
        StartScreenActions.OPEN_STATISTICS
    ))
    drawRect(surface, BUTTON_COLOR, statisticsButton, 0, statisticsButton.height // 6)
    surface.blit(
        font.render(
            STATISTICS_TXT,
            False,
            TEXT_COLOR
        ),
        (statisticsButton.left + offset, statisticsButton.top + offset)
    )
    exitButton: Rect = Rect(
        shortBackgammonButton.left,
        height - height // 24 * 3,
        shortBackgammonButton.width,
        shortBackgammonButton.height
    )
    clickable.append((
        exitButton,
        StartScreenActions.EXIT
    ))
    drawRect(surface, BUTTON_COLOR, exitButton, 0, exitButton.height // 6)
    surface.blit(
        font.render(
            EXIT_TXT,
            False,
            TEXT_COLOR
        ),
        (exitButton.left + offset, exitButton.top + offset)
    )
    return clickable
# }
