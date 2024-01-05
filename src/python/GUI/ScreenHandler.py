from typing import NoReturn as Unit

import pygame as PyGame
from pygame import Surface
from pygame.event import Event

from src.python.GUI.enums import GameStatus, StartScreenActions
from src.python.GUI.start_screen import handleStartScreenAction, drawStartScreen


class ScreenHandler:  # {
    def __init__(self):  # {
        self.status: GameStatus = GameStatus.START_SCREEN
        self.clickable: list = []
    # }

    def handleEvent(self, event: Event) -> Unit:  # {
        """
        Handle given event and update UI.
        :param event: Event to be handled
        :return: Void (Unit (NoReturn))
        """
        match event.type:  # {
            case PyGame.MOUSEBUTTONDOWN:  # {
                x, y = event.pos
                for it in self.clickable:  # {
                    if (it[0].collidepoint(x, y)):  # {
                        if (it[1] in StartScreenActions):  # {
                            handleStartScreenAction(it[1])
                        # }
                    # }
                # }
            # }
        # }
    # }

    def invalidate(self, surface: Surface) -> Unit:  # {
        """
        Update given surface.
        :param surface: Surface to be invalidated
        :return: Void (Unit (NoReturn))
        """
        if (self.status == GameStatus.START_SCREEN):  # {
            self.clickable = drawStartScreen(surface)
        # }
    # }
# }
