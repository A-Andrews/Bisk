from typing import Set


class Faction:

    def __init__(self, name, colour, starting_territories=None):
        self.name = name
        self.colour = colour
        self.territories = Set()
        self.stockpile = 0
        self.resources = {}
        self.units = {}

    def add_territory(self, territory):
        self.territories.append(territory)
        territory.faction = self

    def remove_territory(self, territory):
        if territory in self.territories:
            self.territories.remove(territory)
            territory.faction = None

    def add_resources(self, resource, amount):
        pass

    def consume_resources(self, resource, amount):
        pass

    def add_to_stockpile(self, amount):
        self.stockpile += amount
