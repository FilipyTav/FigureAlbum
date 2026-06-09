import random

from structs.Figurine import Figurine
from utils.types import FigurineRarity, FootballPosition


class FigurineExamples:
    def __init__(self):
        # fmt: off
        self.cards: dict[int, Figurine] = {
            0: Figurine(0, "Alisson Becker", "Brazil", FootballPosition.GK, FigurineRarity.RARE),
            1: Figurine(1, "Virgil van Dijk", "Netherlands", FootballPosition.CB, FigurineRarity.LEGENDARY),
            2: Figurine(2, "Achraf Hakimi", "Morocco", FootballPosition.RB, FigurineRarity.COMMON),
            3: Figurine(3, "Kevin De Bruyne", "Belgium", FootballPosition.AM, FigurineRarity.LEGENDARY),
            4: Figurine(4, "Jude Bellingham", "England", FootballPosition.CM, FigurineRarity.RARE),
            5: Figurine(5, "Rodri", "Spain", FootballPosition.DM, FigurineRarity.LEGENDARY),
            6: Figurine(6, "Vinícius Júnior", "Brazil", FootballPosition.LW, FigurineRarity.LEGENDARY),
            7: Figurine(7, "Erling Haaland", "Norway", FootballPosition.ST, FigurineRarity.LEGENDARY),
            8: Figurine(8, "Bukayo Saka", "England", FootballPosition.RW, FigurineRarity.RARE),
            9: Figurine(9, "Federico Dimarco", "Italy", FootballPosition.LWB, FigurineRarity.COMMON)
        }
        # fmt: on

    def draw_pack(self, pack_size: int = 5) -> list[Figurine]:
        pool: list[Figurine] = list(self.cards.values())

        weights: list[float] = [card.rarity.weight for card in pool]
        print(weights)

        return random.choices(pool, weights=weights, k=pack_size)

    def get(self, card_id: int) -> Figurine | None:
        return self.cards.get(card_id)
