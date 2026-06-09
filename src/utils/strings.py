import os

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


def print_section_name_full(
    name: str, sub: bool = False, color: Colors = Colors.MAGENTA
) -> None:
    # 1. Get the current, real-time terminal width (fallback to 80 if running inside an IDE console)
    try:
        term_width = os.get_terminal_size().columns
    except OSError:
        term_width = 80

    # 2. Determine your separator character based on the 'sub' flag
    # (Assuming SEPARATOR and SUB_SEPARATOR are strings like "=" and "-")
    char = "=" if not sub else "-"

    # 3. Create the full-width separator line
    sep_line = char * term_width

    # 4. Print it out using your exact string centering format modifier `^`
    print(f"\n{color}{Colors.BOLD}{sep_line}")
    print(f"{name:^{term_width}}")
    print(f"{sep_line}{Colors.RESET}\n")


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


def print_centered_header(text: str, fill_char: str = "=") -> None:
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    core_text: str = f" {text} "

    padding_length: int = max(0, (terminal_width - len(core_text)) // 2)

    padding: str = fill_char * padding_length

    full_line: str = f"{padding}{core_text}{padding}"

    if len(full_line) < terminal_width:
        full_line += fill_char

    print(f"\n{Colors.BOLD}{Colors.GOLD}{full_line}{Colors.RESET}")
