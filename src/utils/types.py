from enum import Enum


class Screen(Enum):
    pass


class FigurineRarity(Enum):
    COMMON = ("Common", "#9d9d9d", 70.0)
    RARE = ("Rare", "#0070dd", 25.0)
    LEGENDARY = ("Legendary", "#ff8000", 5.0)

    def __init__(self, display_name: str, color_hex: str, weight: float):
        self._display_name = display_name
        self._color_hex = color_hex
        self._weight = weight

    @property
    def display_name(self) -> str:
        return self._display_name

    @property
    def color(self) -> str:
        return self._color_hex

    @property
    def weight(self) -> float:
        return self._weight


class FootballPosition(Enum):
    # --- GOALKEEPER ---
    GK = ("Goalkeeper", "Goalkeeper")

    # --- DEFENDERS ---
    CB = ("Center-Back", "Defender")
    LB = ("Left-Back", "Defender")
    RB = ("Right-Back", "Defender")
    LWB = ("Left Wing-Back", "Defender")
    RWB = ("Right Wing-Back", "Defender")

    # --- MIDFIELDERS ---
    DM = ("Defensive Midfielder", "Midfielder")
    CM = ("Central Midfielder", "Midfielder")
    AM = ("Attacking Midfielder", "Midfielder")
    LM = ("Left Midfielder", "Midfielder")
    RM = ("Right Midfielder", "Midfielder")

    # --- FORWARDS / ATTACKERS ---
    LW = ("Left Winger", "Forward")
    RW = ("Right Winger", "Forward")
    ST = ("Striker", "Forward")
    CF = ("Center Forward", "Forward")

    def __init__(self, full_name: str, line: str):
        self._full_name = full_name
        self._line = line

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def line(self) -> str:
        return self._line
