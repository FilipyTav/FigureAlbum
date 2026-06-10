import os

from utils.colors import Colors
from utils.strings import (
    print_centered_header,
    print_section_end,
    print_section_end_full,
    print_section_name_full,
)
from utils.types import Screen, ScreenConfig
from utils.input import get_nav_input


def screen_clear():
    os.system("cls" if os.name == "nt" else "clear")


def main_menu(registry: list[ScreenConfig]) -> Screen:
    print_section_name_full("Álbum")
    print("Escolha uma opção: \n")

    # All screens belonging to MAIN
    options: list[ScreenConfig] = [c for c in registry if c.parent == Screen.MAIN]

    # Options
    for i, config in enumerate(options, 1):
        print(f"{Colors.BLUE}{i}{Colors.RESET}. {config.label}")

    print_section_end_full()
    nav, choice = get_nav_input()
    if nav:
        return nav

    # Choice for main options
    try:
        idx: int = int(choice) - 1
        if 0 <= idx < len(options):
            return options[idx].id
    except ValueError:
        pass

    print(f"{Colors.RED}[!] Opção inválida!{Colors.RESET}")
    return Screen.STAY


def todo_screen() -> Screen:
    print_section_name_full("TODO")
    print("Screen yet to be implemented")
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY
