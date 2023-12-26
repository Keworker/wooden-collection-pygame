from enum import Enum


class GameStatus(Enum):  # {
    START_SCREEN = 0
    SHORT_BACKGAMMON = 1
    LONG_BACKGAMMON = 2
    STATISTICS = 3
# }


class StartScreenActions(Enum):  # {
    OPEN_SHORT_BACKGAMMON = 0 * int(10e2)
    OPEN_LONG_BACKGAMMON = 1 * int(10e2)
    OPEN_STATISTICS = 2 * int(10e2)
    EXIT = 3 * int(10e2)
# }
