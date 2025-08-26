import pygame as pg

from settings import FG, HEIGHT, WIDTH
from src.core.scene import Scene


class GameScene(Scene):
    def enter(self):
        self.font = pg.font.Font(None, 36)

    def handle_event(self, e):
        if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            from src.ui.start_screen import StartMenu

            self.game.set_scene(StartMenu)

    def draw(self, surf):
        surf.fill((10, 12, 18))
        msg = self.font.render("Playing…", True, FG)
        surf.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
