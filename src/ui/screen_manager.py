import os

from structs.Album import FigurineAlbum
from structs.Figurine import Figurine
from utils.colors import Colors
from utils.figurine_examples import FigurineExamples
from utils.strings import (
    centered_msg,
    centered_msg_full,
    format_error,
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
    print(f"\n{Colors.UNDERLINE}Figurinha #{id} adicionada com sucesso!{Colors.RESET}")

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


def alb_display(album: FigurineAlbum) -> Screen:
    screen_clear()

    print_section_name_full("ÁLBUM DE FIGURINHAS")
    print(centered_msg_full("Suas figuinhas"))

    for f in album.get_figurines():
        f.display_as_card()

    print("Total: ", album.len())
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY


def alb_rm_fig(album: FigurineAlbum) -> Screen:
    screen_clear()

    print_section_name_full("REMOVER FIGURINHAS")
    print(centered_msg_full("Qual remover?"))

    for f in album.get_figurines():
        f.display_as_card()

    print("Total: ", album.len())

    print_section_end_full()

    id_str: str | None = get_and_validate_input(
        "ID", create_range_validator(0, album.len() - 1), cancel_key="B"
    )

    if not id_str or id_str == "b":
        return Screen.BACK

    id: int = int(id_str)

    album.remove_all_copies(id)
    print(
        f"\n{Colors.UNDERLINE}Figurinha #{id} removida em sua totalidade com sucesso!{Colors.RESET}"
    )

    print()
    print_section_end_full()

    print("\n[A] Remover outra")
    nav, choice = get_nav_input(False)
    if nav:
        return nav

    match choice:
        case "a":
            return Screen.STAY

    return Screen.BACK


def alb_find_fig(album: FigurineAlbum) -> Screen:
    screen_clear()

    print_section_name_full("CONSULTAR FIGURINHA")
    print(centered_msg_full("Como consultar?"))

    if album.is_empty():
        print(centered_msg("Álbum vazio"))
        print_section_end_full()

        nav, _ = get_nav_input()
        if nav:
            return nav

    op: str | None = get_and_validate_input(
        "Buscar por ID[1] | Nome[2] | Seleção[3]",
        create_range_validator(1, 3),
        "Escolha uma das opções",
        cancel_key="B",
    )

    if not op:
        return Screen.BACK

    error_msg: str = ""
    match op:
        case "1":
            id_str: str | None = get_and_validate_input(
                f"Busca por {Colors.BOLD}ID{Colors.RESET}[{0}, {album.len() - 1}]",
                create_range_validator(0, album.len() - 1),
                "ID deve ser um número natural entre [0, 2]!",
                cancel_key="B",
            )

            if not id_str:
                return Screen.BACK

            id: int = int(id_str)

            fig: Figurine | None = album.find_by_id(id)
            if fig:
                print_section_end_full()
                print()
                fig.display_as_card()
            else:
                error_msg = f"Não foi possível encontrar figurinha (ID:{id}) no álbum."

        case "2":
            name: str | None = get_and_validate_input(
                f"Busca por {Colors.BOLD}Nome{Colors.RESET}",
                None,
                "Nome não pode estar vazio!",
                cancel_key="B",
            )

            if not name:
                return Screen.BACK

            fig: Figurine | None = album.find_by_name(name)

            if fig:
                print_section_end_full()
                print()
                fig.display_as_card()
            else:
                error_msg = f"Não foi possível encontrar '{name}' no álbum."

        case "3":
            pass

        case _:
            print(format_error(error_msg))

    if error_msg:
        print()
        print(format_error(error_msg))

    print_section_end_full()

    print("\n[A] Consultar outra")
    nav, choice = get_nav_input(False)
    if nav:
        return nav

    match choice:
        case "a":
            return Screen.STAY

    return Screen.BACK


def todo_screen() -> Screen:
    print_section_name_full("TODO")
    print("Screen yet to be implemented")
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY
