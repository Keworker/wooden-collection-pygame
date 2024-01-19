import random

from src.python.core.Dice import Dice


SEEDS: list[int] = [
    10009, 10009 * 2, 10009 * 3, 10009 * 6,
    100000007, 100000007 * 2, 100000007 * 3, 100000007 * 6
]


class RandomDice(Dice):  # {
    def __init__(self):  # {
        seed: int = random.choice(SEEDS)
        randomValue: int = random.randint(1, 6)
        self.__value: int = seed * randomValue % 6 + 1
    # }

    # @Override
    def getValue(self) -> int:  # {
        """
        overriden
        :return:
        """
        return self.__value
    # }
# }
