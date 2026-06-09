from enum import Enum


class Colors(Enum):
    # Colors
    BLUE = "\033[94m"
    GOLD = "\033[93m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    GREEN = "\033[32m"
    LIGHT_GREEN = "\033[92m"
    WHITE = "\033[97m"
    LIGHT_GRAY = "\033[37m"
    DARK_GRAY = "\033[90m"
    BLACK = "\033[30m"

    # Formatting
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"
    REVERSE = "\033[7m"
    RESET = "\033[0m"

    # Background
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_LIGHT_GRAY = "\033[47m"
    BG_BLUE = "\033[104m"
    BG_GOLD = "\033[103m"

    def __str__(self) -> str:
        return self.value
