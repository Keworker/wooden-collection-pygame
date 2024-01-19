from typing import NoReturn as Unit

from pygame import Surface, Color, Rect
from pygame.draw import polygon as drawPolygon, line as drawLine, circle as drawCircle, rect as drawRect

from src.python.GUI.Circle import Circle
from src.python.GUI.colors import BACKGAMMON_BACKGROUND_COLOR, BACKGAMMON_BLACK_BACKGROUND_COLOR, \
    BACKGAMMON_WHITE_BACKGROUND_COLOR, BACKGAMMON_BLACK_FOREGROUND_COLOR, \
    BACKGAMMON_WHITE_FOREGROUND_COLOR, RED
from src.python.GUI.enums import BackgammonActions
from src.python.core.Chip import ChipColor, Chip


# noinspection PyTypeChecker
screenSize: tuple = None


def drawBackgammonBackground(surface: Surface) -> Unit:  # {
    """
    Draws background for the backgammon game.
    :param surface: Surface for drawing
    :return: Unit
    """
    surface.fill(BACKGAMMON_BACKGROUND_COLOR)
    triangleWidth: float = screenSize[0] / 12
    triangleHeight: float = screenSize[1] / 3
    bottom: float = screenSize[1]
    blackBackgroundC: Color = Color(*BACKGAMMON_BLACK_BACKGROUND_COLOR)
    whiteBackgroundC: Color = Color(*BACKGAMMON_WHITE_BACKGROUND_COLOR)
    for i in range(0, 24, +1):  # {
        if (i % 2 == 0):  # {
            color1: Color = whiteBackgroundC
            color2: Color = blackBackgroundC
        # }
        else:  # {
            color1: Color = blackBackgroundC
            color2: Color = whiteBackgroundC
        # }
        drawPolygon(
            surface,
            color1,
            [
                (triangleWidth * i, 0),
                (triangleWidth * (i + 1) - 1, 0),
                (triangleWidth * i + triangleWidth / 2, triangleHeight)
            ]
        )
        drawPolygon(
            surface,
            color2,
            [
                (triangleWidth * i, bottom),
                (triangleWidth * (i + 1) - 1, bottom),
                (triangleWidth * i + triangleWidth / 2, bottom - triangleHeight)
            ]
        )
    # }
    drawLine(
        surface,
        blackBackgroundC,
        (screenSize[0] / 2, 0),
        (screenSize[0] / 2, bottom)
    )
# }


def drawChip(cords: tuple[int, int], color: ChipColor, surface: Surface, drawDirect: bool = False) -> tuple:  # {
    """
    Draws a chip at given position.
    :param cords: Position of chip in our backgammon notation
    :param color: Color of chip (ChipColor)
    :param surface: Surface for drawing
    :param drawDirect: If true, draw the chip at the given cords on screen
    :return: Clickable object of chip
    """
    triangleWidth: float = screenSize[0] / 12
    chipSize: float = screenSize[1] / 30
    color: Color = Color(BACKGAMMON_WHITE_FOREGROUND_COLOR) \
        if color is ChipColor.WHITE else \
        Color(BACKGAMMON_BLACK_FOREGROUND_COLOR)
    if (drawDirect):  # {
        x = cords[0]
        y = cords[1]
    # }
    elif (cords[0] < 12):  # {
        y: float = chipSize * cords[1] + chipSize / 2
        x: float = screenSize[0] - triangleWidth * cords[0] - triangleWidth / 2
    # }
    else:  # {
        y: float = screenSize[1] - chipSize * cords[1] - chipSize / 2
        x: float = triangleWidth * (cords[0] - 12) + triangleWidth / 2

    # }
    drawCircle(surface, color, (x, y), chipSize / 2)
    return Circle((x, y), chipSize / 2, [cords, color]), BackgammonActions.HOLD_CHIP
# }


def drawExitButton(surface: Surface) -> tuple:  # {
    """
    Draws exit button on the surface.
    :param surface: Surface for drawing
    :return: Clickable object
    """
    size: float = screenSize[1] / 30
    rect: Rect = Rect(screenSize[0] / 2 - size / 2, screenSize[1] / 2 - size / 2, size, size)
    drawRect(surface, RED, rect, border_radius=int(size / 6))
    return rect, BackgammonActions.EXIT
# }


def drawBackgammon(surface: Surface, gameData: list) -> list:  # {
    """
    Draws backgammon on the given surface.
    :param surface: Surface for drawing
    :param gameData: List with game data from screen handler
    :return: List of clickable objects on screen
    """
    global screenSize
    if (screenSize is None):  # {
        screenSize = surface.get_size()
    # }
    drawBackgammonBackground(surface)
    clickable: list = [drawExitButton(surface)]
    field: Backgammon = gameData[0]
    if not (field.isAssociatedWithPlane()):  # {
        field.associateWithPlane(*screenSize)
        gameData[2][1][0].setBorders((0, 0), screenSize)
        gameData[2][1][1].setBorders((0, 0), screenSize)
    # }
    actionChips: list[Chip] = list()
    for i, position in enumerate(field.getField()):  # {
        for j, chip in enumerate(position):  # {
            if not (chip.inAction):  # {
                clickable.append(drawChip((i, j), chip.color, surface))
            # }
            else:  # {
                actionChips.append(chip)
            # }
        # }
    # }
    if (actionChips):  # {
        drawChip(gameData[3], actionChips[0].color, surface, True)
    # }
    return clickable[::-1]
# }
