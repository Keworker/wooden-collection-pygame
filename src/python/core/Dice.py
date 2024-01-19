from abc import ABC as ABSTRACT, abstractmethod as abstract


class Dice(ABSTRACT):  # {
    @abstract
    def getValue(self) -> int:  # {
        """
        Returns value at the top of dice.
        :return: value at top of dice (form 1 to 6)
        """
    # }
# }
