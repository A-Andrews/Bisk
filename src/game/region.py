class Region:
    def __init__(self, name, resources, terrain_type, faction=None):
        self.name = name
        self.resources = resources
        self.faction = faction
        self.terrain_type = terrain_type
