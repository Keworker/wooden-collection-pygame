from copy import deepcopy


class Circle:  # {
    def __init__(self, center: tuple[float, float], radius: float, data: list):  # {
        self.__center: tuple[float, float] = center
        self.__radius: float = radius
        self.__data: list = data
    # }

    def getData(self) -> list:  # {
        """
        Returns additional data of circle.
        :return: list of data
        """
        return deepcopy(self.__data)
    # }

    def collidepoint(self, x, y) -> bool:  # {
        """
        Returns True, if given point is in area of circle, else, returns false.
        :param x: x cord of point
        :param y: y cord of point
        :return: boolean value
        """
        return (x - self.__center[0]) ** 2 + (y - self.__center[1]) ** 2 <= self.__radius ** 2
    # }
# }
