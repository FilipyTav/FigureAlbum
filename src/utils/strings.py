from utils.colors import Colors


def clean_string(string: str, lcase: bool = True):
    return string.strip().lower() if lcase else string.strip()


NAV_PROMPT: str = "\n[B] Voltar | [M] Início | [Q] Sair\n> "

SEPARATOR_WIDTH: int = 45
SEPARATOR: str = "=" * SEPARATOR_WIDTH
SUB_SEPARATOR: str = "-" * SEPARATOR_WIDTH


def print_section_name(
    name: str, sub: bool = False, color: Colors = Colors.MAGENTA
) -> None:
    sep: str = SEPARATOR if not sub else SUB_SEPARATOR

    print(f"\n{color}{Colors.BOLD}" + sep)
    print(f"{Colors.BOLD}{name:^{SEPARATOR_WIDTH}}")
    print(sep + f"{Colors.RESET}\n")


def print_section_end(sub: bool = False, color: Colors = Colors.MAGENTA) -> None:
    sep: str = SEPARATOR if not sub else SUB_SEPARATOR

    print(f"\n{color}{Colors.BOLD}{sep}{Colors.RESET}")


def format_error(msg: str) -> str:
    return f"  {Colors.RED}[!] {msg} [!]{Colors.RESET}"


def centered_msg(
    msg: str, width: int = SEPARATOR_WIDTH, color: Colors = Colors.YELLOW
) -> str:
    return f"{color}{Colors.BOLD}{f'{msg}':^{width}}{Colors.RESET}"


def truncate_string(text: str, max_width: int, suffix: str = "...") -> str:
    return text[: max_width - len(suffix)] + suffix if len(text) > max_width else text


def get_visible_len(text: str) -> int:
    """Ignores ANSI codes"""
    length: int = 0
    is_escape: bool = False

    for char in text:
        if char in ("\033", "\x1b"):
            is_escape = True
        elif is_escape:
            if char == "m":
                is_escape = False
        else:
            length += 1

    return length
