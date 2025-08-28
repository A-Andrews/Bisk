from src.game.unit import Unit


class Territory:
    def __init__(self, name: str):
        self.name: str = name
        self.resources: dict[str, int] = {}
        self.units: list[Unit] = []
