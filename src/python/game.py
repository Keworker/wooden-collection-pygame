import sys as System

import pygame as PyGame
from pygame import Surface
from pygame.time import Clock
from pygame.sprite import Group

from src.python.GUI.ScreenHandler import ScreenHandler


if __name__ == '__main__':  # {
    PyGame.init()
    screen: Surface = PyGame.display.set_mode(flags=PyGame.FULLSCREEN)
    handler: ScreenHandler = ScreenHandler()
    handler.invalidate(screen)
    clock: Clock = Clock()
    allSprites: Group = Group()
    running: bool = True
    while running:  # {
        try:  # {
            for event in PyGame.event.get():  # {
                if (event == PyGame.QUIT):  # {
                    raise KeyboardInterrupt()
                # }
                handler.handleEvent(event, allSprites)
            # }
            handler.invalidate(screen)
            allSprites.update(clock.tick())
            allSprites.draw(screen)
            PyGame.display.flip()
        # }
        except KeyboardInterrupt:  # {
            running = False
        # }
    # }
    PyGame.quit()
    System.exit()
# }
