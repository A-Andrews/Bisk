from pygame.color import Color
import pygame as pg
from src.game.faction import Faction
from src.game.region import Region
from src.game.territory import Territory
from pygame.surface import Surface
from pygame import Rect
from settings import (
    WIDTH,
    HEIGHT,
    BOARD_X_DIM,
    BOARD_Y_DIM,
    BOARD_PADDING,
    FG,
)
from random import randint

CELL_WIDTH = (WIDTH - BOARD_PADDING * 2) / BOARD_X_DIM
CELL_HEIGHT = (HEIGHT - BOARD_PADDING * 2) / BOARD_Y_DIM


class Board:
    def __init__(self):
        self.regions = regions

        # TODO randomly assign resources on each territory
        for r in self.regions:
            for t in r.territories:
                t.resources = {
                    "flour": randint(0, 5),
                    "sugar": randint(0, 5),
                    "butter": randint(0, 5),
                    "cocoa": randint(0, 5),
                    "cream": randint(0, 5),
                }

        # TODO place territories on board (randomly...)
        board_cells: list[list[Territory | None]] = [
            [None for _ in range(BOARD_X_DIM)] for _ in range(BOARD_Y_DIM)
        ]
        c = 0
        for r in self.regions:
            for t in r.territories:
                m, n = c // BOARD_Y_DIM - 1, c % BOARD_X_DIM
                board_cells[m][n] = t
                c += 1
        del c

        # TODO randomly assign borders to territories (with validation that graph is connected)
        graph = [[0 for _ in range(n)] for _ in range(n)]

    def draw(self, surf: Surface):
        # TODO draw territories
        for i, r in enumerate(self.regions):
            for j, t in enumerate(r.territories):
                position = (
                    BOARD_PADDING + (CELL_WIDTH * i) + 10,
                    BOARD_PADDING + (CELL_HEIGHT * j) + 10,
                )
                rect = Rect(
                    position,
                    (CELL_WIDTH - 10, CELL_HEIGHT - 10),
                )
                pg.draw.rect(surf, r.color, rect)
                msg = pg.font.Font(None, 18).render(
                    f"{r.name} - {t.name}", True, FG
                )
                surf.blit(msg, msg.get_rect(center=rect.center))

        # TODO draw borders

        # TODO draw text overlay


f1 = Faction(name="McVitites Kingdom", colour=Color(255, 0, 0))
f2 = Faction(name="Fox-Burton Commonwealth", colour=Color(0, 255, 0))
f3 = Faction(name="Republic of Border", colour=Color(0, 0, 255))

factions = [f1, f2, f3]

r1 = Region(
    name="Edinburgh",
    color=Color(100, 100, 100),
    territories=[
        Territory(**x)
        for x in [
            {"name": "Jamville"},
            {"name": "Coffeeland"},
            {"name": "Bourbonia"},
            {"name": "CookieMilk"},
        ]
    ],
)
r2 = Region(
    name="York",
    color=Color(100, 100, 100),
    territories=[Territory(name=f"Territory {i}") for i in range(4)],
)
r3 = Region(
    name="Blackpool",
    color=Color(100, 100, 100),
    territories=[Territory(name=f"Territory {i}") for i in range(4)],
)
r4 = Region(
    name="Reading",
    color=Color(100, 100, 100),
    territories=[Territory(name=f"Territory {i}") for i in range(4)],
)
r5 = Region(
    name="London",
    color=Color(100, 100, 100),
    territories=[Territory(name=f"Territory {i}") for i in range(4)],
)

regions = [r1, r2, r3, r4, r5]
