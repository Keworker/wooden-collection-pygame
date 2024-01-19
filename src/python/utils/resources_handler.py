import os

import pygame as PyGame
from pygame import Surface


def getFont(name: str = "Roboto-Regular.ttf") -> str:  # {
    """
    Returns path to font file (by default 'Roboto-Regular' font).
    :param name: Name of font
    :return: Path to the `.ttf` file
    """
    localPath: str = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    return os.path.join(localPath, "res", name)
# }


def getImage(name: str) -> Surface:  # {
    """
    Returns path to image file
    :param name: Name of image resource
    :return: Path to `.png` file
    """
    localPath: str = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    return PyGame.image.load(os.path.join(localPath, "res", name))
# }


def getDatabasePath() -> str:  # {
    """
    Returns absolute path to database file
    :return: string path
    """
    return os.path.join(
        os.path.split(os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0])[0],
        "database.sql"
    )
# }
