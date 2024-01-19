from src.python.core.Dice import Dice


class ConstantDice(Dice):  # {
    def __init__(self, value: int):  # {
        self.__value = value
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
