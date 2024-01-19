from enum import Enum


class GameStatus(Enum):  # {
    START_SCREEN = 1
    SHORT_BACKGAMMON = 2
    LONG_BACKGAMMON = 3
    STATISTICS = 4
# }


class StartScreenActions(Enum):  # {
    OPEN_SHORT_BACKGAMMON = 1 * int(10e2)
    OPEN_LONG_BACKGAMMON = 2 * int(10e2)
    OPEN_STATISTICS = 3 * int(10e2)
    EXIT = 4 * int(10e2)
# }


class BackgammonActions(Enum):  # {
    HOLD_CHIP = 4 * int(10e4)
    MOVE_CHIP = 5 * int(10e4)
    DROP_CHIP = 6 * int(10e4)
    EXIT = 7 * int(10e4)
# }


class StatisticsActions(Enum):  # {
    EXIT = 1 * int(10e6)
# }
