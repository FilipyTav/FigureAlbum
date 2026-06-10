import random

from structs.Figurine import Figurine
from utils.types import FigurineRarity, FootballPosition


class FigurineExamples:
    # fmt: off
    DATA_POOL = {
        0: ("Alisson Becker", "Brazil", FootballPosition.GK, FigurineRarity.RARE),
        1: ("Virgil van Dijk", "Netherlands", FootballPosition.CB, FigurineRarity.LEGENDARY),
        2: ("Achraf Hakimi", "Morocco", FootballPosition.RB, FigurineRarity.COMMON),
        3: ("Kevin De Bruyne", "Belgium", FootballPosition.AM, FigurineRarity.LEGENDARY),
        4: ("Jude Bellingham", "England", FootballPosition.CM, FigurineRarity.RARE),
        5: ("Rodri", "Spain", FootballPosition.DM, FigurineRarity.LEGENDARY),
        6: ("Vinícius Júnior", "Brazil", FootballPosition.LW, FigurineRarity.LEGENDARY),
        7: ("Erling Haaland", "Norway", FootballPosition.ST, FigurineRarity.LEGENDARY),
        8: ("Bukayo Saka", "England", FootballPosition.RW, FigurineRarity.RARE),
        9: ("Federico Dimarco", "Italy", FootballPosition.LWB, FigurineRarity.COMMON)
    }
    # fmt: on

    def __init__(self) -> None:
        self.cards: dict[int, Figurine] = {
            card_id: Figurine(card_id, *info)
            for card_id, info in self.DATA_POOL.items()
        }

    def draw_pack(self, pack_size: int = 5) -> list[Figurine]:
        pool: list[Figurine] = list(self)
        weights: list[float] = [card.rarity.weight for card in pool]

        return random.choices(pool, weights=weights, k=pack_size)

    def get(self, card_id: int) -> Figurine | None:
        return self.cards.get(card_id)

    def __iter__(self):
        return iter(self.cards.values())
