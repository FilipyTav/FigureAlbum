from enum import Enum, auto

from utils.colors import Colors


class Screen(Enum):
    # Helpers
    # ------------------------
    MAIN = auto()
    BACK = auto()
    EXIT = auto()
    STAY = auto()
    TODO = auto()
    # ------------------------


class FigurineRarity(Enum):
    # COMMON = ("Common", "#9d9d9d", 70.0)
    # RARE = ("Rare", "#0070dd", 25.0)
    # LEGENDARY = ("Legendary", "#ff8000", 5.0)

    # COMMON = ("Common", Colors.LIGHT_GRAY, 70.0)
    # RARE = ("Rare", Colors.BLUE, 25.0)
    # LEGENDARY = ("Legendary", Colors.GOLD, 5.0)

    # Format: (Display Name, Color Enum Code, Color BG code, Drop Weight)
    COMMON = ("Common", Colors.LIGHT_GRAY, Colors.BG_LIGHT_GRAY, 70.0)
    RARE = ("Rare", Colors.BLUE, Colors.BG_BLUE, 25.0)
    LEGENDARY = ("Legendary", Colors.GOLD, Colors.BG_GOLD, 5.0)

    def __init__(
        self, display_name: str, fgcolor: Colors, bgcolor: Colors, weight: float
    ):
        self._display_name: str = display_name
        self._fgcolor: Colors = fgcolor
        self._bgcolor: Colors = bgcolor
        self._weight: float = weight

    @property
    def display_name(self) -> str:
        return self._display_name

    @property
    def fgcolor(self) -> Colors:
        return self._fgcolor

    @property
    def bgcolor(self) -> Colors:
        return self._bgcolor

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
