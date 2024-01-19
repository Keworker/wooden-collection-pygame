from typing import NoReturn as Unit

import pygame as PyGame
from pygame import Surface
from pygame.event import Event
from pygame.sprite import Group

from src.python.GUI.enums import GameStatus, StartScreenActions, \
    BackgammonActions, StatisticsActions
from src.python.GUI.backgammon import drawBackgammon
from src.python.GUI.backgammon import handleBackgammonAction
from src.python.GUI.start_screen import handleStartScreenAction, drawStartScreen
from src.python.GUI.statistics import drawStatistics


class ScreenHandler:  # {
    def __init__(self):  # {
        self.status: GameStatus = GameStatus.START_SCREEN
        self.clickable: list = []
        self.gameData = None
    # }

    def handleEvent(self, event: Event, allSprites: Group) -> Unit:  # {
        """
        Handle given event and update UI.
        :param event: Event to be handled
        :param allSprites: Group of all game sprites
        :return: Unit
        """
        match event.type:  # {
            case PyGame.MOUSEBUTTONDOWN:  # {
                x, y = event.pos
                for it in self.clickable:  # {
                    if (it[0].collidepoint(x, y)):  # {
                        if (it[1] in StartScreenActions):  # {
                            self.status, self.gameData = handleStartScreenAction(it[1], allSprites)
                        # }
                        elif (it[1] in BackgammonActions):  # {
                            if (self.status == GameStatus.LONG_BACKGAMMON):  # {
                                self.status, self.gameData = handleBackgammonAction(
                                    it[1], self.gameData, it[0], (x, y), event.type
                                )
                            # }
                            else:  # {
                                self.status, self.gameData = handleBackgammonAction(
                                    it[1], self.gameData, it[0], (x, y), event.type
                                )
                            # }
                        # }
                        elif (it[1] in StatisticsActions):  # {
                            self.status, self.gameData = GameStatus.START_SCREEN, []
                        # }
                    # }
                # }
                if (self.status == GameStatus.LONG_BACKGAMMON or
                        self.status == GameStatus.SHORT_BACKGAMMON):  # {
                    if (self.gameData[2][1][0].collidepoint(x, y)):  # {
                        self.gameData[2] = (
                            (self.gameData[1](), self.gameData[2][0][1]), self.gameData[2][1]
                        )
                        self.gameData[2][1][0].setNumber(self.gameData[2][0][0].getValue())
                        self.gameData[2][1][0].hold((x, y))
                    # }
                    elif (self.gameData[2][1][1].collidepoint(x, y)):  # {
                        self.gameData[2] = (
                            (self.gameData[2][0][0], self.gameData[1]()), self.gameData[2][1]
                        )
                        self.gameData[2][1][1].setNumber(self.gameData[2][0][1].getValue())
                        self.gameData[2][1][1].hold((x, y))
                    # }
                # }
            # }
            case PyGame.MOUSEMOTION | PyGame.MOUSEBUTTONUP:  # {
                x, y = PyGame.mouse.get_pos()
                if (self.status == GameStatus.LONG_BACKGAMMON or
                        self.status == GameStatus.SHORT_BACKGAMMON):  # {
                    if (self.gameData[2][1][0].wasHold() and
                            event.type == PyGame.MOUSEBUTTONUP):  # {
                        self.gameData[2][1][0].drop((x, y))
                    # }
                    elif (self.gameData[2][1][1].wasHold() and
                          event.type == PyGame.MOUSEBUTTONUP):  # {
                        self.gameData[2][1][1].drop((x, y))
                    # }
                    elif (len(self.gameData) > 3):  # {
                        if (self.status == GameStatus.LONG_BACKGAMMON):  # {
                            self.status, self.gameData = handleBackgammonAction(
                                BackgammonActions.MOVE_CHIP, self.gameData,
                                None, (x, y), event.type
                            )
                        # }
                        else:  # {
                            self.status, self.gameData = handleBackgammonAction(
                                BackgammonActions.MOVE_CHIP, self.gameData,
                                None, (x, y), event.type
                            )
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
        :return: Unit
        """
        match self.status:  # {
            case GameStatus.START_SCREEN:  # {
                self.clickable = drawStartScreen(surface)
            # }
            case GameStatus.LONG_BACKGAMMON:  # {
                self.clickable = drawBackgammon(surface, self.gameData)
            # }
            case GameStatus.SHORT_BACKGAMMON:  # {
                self.clickable = drawBackgammon(surface, self.gameData)
            # }
            case GameStatus.STATISTICS:  # {
                self.clickable = drawStatistics(surface)
            # }
        # }
    # }
# }
