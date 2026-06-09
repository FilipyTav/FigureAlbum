from utils.types import FigurineRarity, FootballPosition


class Figurine:
    def __init__(
        self,
        id: int,
        name: str,
        country: str,
        position: FootballPosition,
        rarity: FigurineRarity,
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.country: str = country
        self.position: FootballPosition = position
        self.rariry: FigurineRarity = rarity
