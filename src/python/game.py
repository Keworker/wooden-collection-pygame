import sys as System

import pygame as PyGame
from pygame import Surface

from src.python.GUI.ScreenHandler import ScreenHandler

if __name__ == '__main__':  # {
    PyGame.init()
    size: tuple[int, int] = (1920, 1080)
    screen: Surface = PyGame.display.set_mode(size, PyGame.FULLSCREEN)
    handler: ScreenHandler = ScreenHandler()
    handler.invalidate(screen)
    running: bool = True
    while running:  # {
        try:  # {
            for event in PyGame.event.get():  # {
                if (event == PyGame.QUIT):  # {
                    raise KeyboardInterrupt()
                # }
                handler.handleEvent(event)
            # }
            handler.invalidate(screen)
            PyGame.display.flip()
        # }
        except KeyboardInterrupt:  # {
            running = False
        # }
    # }
    PyGame.quit()
    System.exit()
# }
