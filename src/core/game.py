import sys

import pygame as pg

from settings import FPS, HEIGHT, TITLE, WIDTH
from src.core.handle_input import handle_input


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.flags = pg.SCALED | pg.RESIZABLE
        self.running = True
        self.scene = None
        self.is_fullscreen = False
        self.width = WIDTH
        self.height = HEIGHT

    def set_scene(self, scene_cls, *args, **kwargs):
        if self.scene:
            self.scene.exit()
        self.scene = scene_cls(self, *args, **kwargs)
        self.scene.enter()

    def run(self, first_scene_cls):
        self.set_scene(first_scene_cls)
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            handle_input(self)
            self.scene.update(dt)
            self.scene.draw(self.screen)
            pg.display.flip()
        pg.quit()
        sys.exit(0)
