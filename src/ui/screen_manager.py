import os

from structs.Album import FigurineAlbum
from structs.Figurine import Figurine
from utils.colors import Colors
from utils.figurine_examples import FigurineExamples
from utils.strings import (
    centered_msg,
    centered_msg_full,
    print_centered_header,
    print_section_end,
    print_section_end_full,
    print_section_name_full,
)
from utils.types import Screen, ScreenConfig
from utils.input import create_range_validator, get_and_validate_input, get_nav_input


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


def alb_add_fig(album: FigurineAlbum, fig_pool: FigurineExamples) -> Screen:
    screen_clear()

    print_section_name_full("ADICIONAR FIGUINHA")
    print(centered_msg_full("Escolha"))

    for f in fig_pool:
        f.display_as_card()

    print_section_end_full()

    id_str: str | None = get_and_validate_input(
        "ID", create_range_validator(0, fig_pool.len() - 1), cancel_key="B"
    )

    if not id_str or id_str == "b":
        return Screen.BACK

    id: int = int(id_str)

    album.append(fig_pool.get(id))

    print()
    print_section_end_full()

    print("\n[A] Adicionar outra")
    nav, choice = get_nav_input(False)
    if nav:
        return nav

    match choice:
        case "a":
            return Screen.STAY

    return Screen.BACK

    return Screen.BACK


def todo_screen() -> Screen:
    print_section_name_full("TODO")
    print("Screen yet to be implemented")
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY
