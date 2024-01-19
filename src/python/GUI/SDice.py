from random import random, randint
from typing import NoReturn as Unit

from pygame.sprite import Sprite
from pygame.transform import rotate

from src.python.core.Vector import Vector
from src.python.utils.resources_handler import getImage


class SDice(Sprite):  # {
    IMAGES: list = [
        getImage("dice1.png"),
        getImage("dice2.png"),
        getImage("dice3.png"),
        getImage("dice4.png"),
        getImage("dice5.png"),
        getImage("dice6.png")
    ]

    def __init__(self, group, value: int, cords: tuple):  # {
        super().__init__(group)
        self.__value: int = value
        self.image = SDice.IMAGES[value - 1]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = cords
        self.__rolling: float = 0
        self.__deltaRollingCoefficient: float = 0
        self.__leftUp: tuple[int, int] = (0, 0)
        self.__rightDown: tuple[int, int] = (0, 0)
        self.__speed: Vector = Vector(0, 0)
        self.__acceleration: float = 0
        # noinspection PyTypeChecker
        self.__savedState: tuple[float, float] = None
    # }

    def setNumber(self, value: int) -> Unit:  # {
        """
        Sets the value at the top of dice to given number.
        :param value: int from 1 to 6
        :return: Unit
        """
        self.__value: int = value
        self.image = SDice.IMAGES[value - 1]
    # }

    def setBorders(self, leftUp: tuple[int, int], rightDown: tuple[int, int]) -> Unit:  # {
        """
        Sets sprites motion borders to rect from left up to right down.
        :param leftUp: tuple of x and y cords of left up point
        :param rightDown: tuple of x and y cords of right down point
        :return: Unit
        """
        self.__leftUp = leftUp
        self.__rightDown = rightDown
    # }

    def hold(self, cords: tuple[float, float]) -> Unit:  # {
        """
        Message, that mouse button down at this sprite.
        :param cords: Cords of mouse click
        :return: Unit
        """
        self.__savedState = cords
    # }

    def wasHold(self) -> bool:  # {
        """
        Returns true, if mouse button was pressed at this dice and was not upped.
        :return: boolean
        """
        return self.__savedState is not None
    # }

    def drop(self, cords: tuple[float, float]) -> Unit:  # {
        """
        Starts motion of this dice sprite.
        :param cords: Cords of mouse button up
        :return: Unit
        """
        if (self.__savedState):  # {
            self.__acceleration = 0.95
            self.__speed = (Vector(*cords) - Vector(*self.__savedState)) * self.__acceleration * 3
            self.__rolling = randint(15, 30)
            self.__deltaRollingCoefficient = 0.66 * random()
            self.__savedState = None
        # }
    # }

    # @Override
    def update(self, *args, **kwargs):  # {
        """
        overriden
        :param args:
        :param kwargs:
        :return:
        """
        if (self.__rolling or self.__speed.x or self.__speed.y):  # {
            tick: int = args[0]
            position: Vector = Vector(self.rect.x, self.rect.y)
            position += self.__speed * tick * 0.01
            self.__speed *= self.__acceleration
            if (self.__speed.length() < 0.001):  # {
                self.__speed = Vector(0, 0)
                self.__acceleration = 0
            # }
            self.rect.x = position.x
            self.rect.y = position.y
            if (self.rect.x < self.__leftUp[0]):  # {
                self.__speed.x = -self.__speed.x
                self.rect.x = self.__leftUp[0]
            # }
            elif (self.rect.x > self.__rightDown[0] - self.rect.width):  # {
                self.__speed.x = -self.__speed.x
                self.rect.x = self.__rightDown[0] - self.rect.width
            # }
            if (self.rect.y < self.__leftUp[1]):  # {
                self.__speed.y = -self.__speed.y
                self.rect.y = self.__leftUp[1]
            # }
            elif (self.rect.y > self.__rightDown[1] - self.rect.height):  # {
                self.__speed.y = -self.__speed.y
                self.rect.y = self.__rightDown[1] - self.rect.height
            # }
            self.image = rotate(self.image, self.__rolling * tick * 0.1)
            self.rect = self.image.get_rect(center=self.rect.center)
            self.__rolling *= self.__deltaRollingCoefficient
            if (self.__rolling < 10):  # {
                self.__rolling = 0
                self.__deltaRollingCoefficient = 0
            # }
        # }
    # }

    def collidepoint(self, x: float, y: float) -> bool:  # {
        """
        Returns True, if given point is in area of circle, else, returns false.
        :param x: x cord of point
        :param y: y cord of point
        :return: boolean value
        """
        return self.rect.collidepoint(x, y)
    # }

    def getValue(self) -> int:  # {
        """
        Returns value, that at this dice right now
        :return: int value
        """
        return self.__value
    # }
# }
