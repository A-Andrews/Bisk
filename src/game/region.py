from src.game.territory import Territory
from pygame.color import Color


class Region:
    def __init__(
        self,
        name,
        territories: list[Territory],
        color: Color,
        resources=None,
        terrain_type=None,
        faction=None,
    ):
        self.name = name
        self.territories = territories
        self.color = color
        self.resources = resources
        self.faction = faction
        self.terrain_type = terrain_type
