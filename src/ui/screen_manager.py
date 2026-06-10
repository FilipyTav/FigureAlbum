import os

from structs.Album import FigurineAlbum
from structs.Figurine import Figurine
from structs.Queue import FigurineQueue
from utils.colors import Colors
from utils.config import TOTAL_FIGURINES
from utils.figurine_examples import FigurineExamples
from utils.strings import (
    SEPARATOR,
    SUB_SEPARATOR,
    centered_msg,
    centered_msg_full,
    format_error,
    print_centered_header,
    print_section_end,
    print_section_end_full,
    print_section_name_full,
)
from utils.types import Screen, ScreenConfig
from utils.input import (
    create_range_validator,
    get_and_validate_input,
    get_nav_input,
    validate_exchange_format,
)


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
            country: str | None = get_and_validate_input(
                f"Busca por {Colors.BOLD}Nome{Colors.RESET}",
                None,
                "Nome não pode estar vazio!",
                cancel_key="B",
            )

            if not country:
                return Screen.BACK

            fig: Figurine | None = album.find_by_name(country)

            if fig:
                print_section_end_full()
                print()
                fig.display_as_card()
            else:
                error_msg = f"Não foi possível encontrar '{country}' no álbum."

        case "3":
            country: str | None = get_and_validate_input(
                f"Busca por {Colors.BOLD}Seleção{Colors.RESET}",
                None,
                "Seleção não pode estar vazia!",
                cancel_key="B",
            )

            if not country:
                return Screen.BACK

            figs: list[Figurine] = album.find_by_country(country)

            if len(figs):
                print_section_end_full()
                print()
                [f.display_as_card() for f in figs]
            else:
                error_msg = f"Não foi possível encontrar seleção '{country}' no álbum."

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


def alb_display_stats(album: FigurineAlbum, fig_pool: FigurineExamples) -> Screen:
    print_section_name_full("Estatísticas")
    print(centered_msg_full("Dados"))
    print_section_end_full()
    print()

    stats: dict = album.get_statistics(fig_pool)

    c = Colors

    print(f"{c.BOLD}Progresso Geral:{c.RESET}")
    print(f"  Concluído:       {c.LIGHT_GREEN}{stats['completion_rate']:.1f}%{c.RESET}")
    print(
        f"  Colecionadas:    {stats['unique_owned']} de {stats['total_pool']} figuras únicas"
    )
    print(f"  Total no album:  {stats['total_items']} unidades totais")
    print(f"  Repetidas:       {c.YELLOW}{stats['duplicates_count']}{c.RESET}")

    print(f"\n{c.DARK_GRAY}------------------------------------------------{c.RESET}")

    print(f"{c.BOLD}Distribuição por Raridade:{c.RESET}")
    if not stats["rarity_distribution"]:
        print(f"  {c.DARK_GRAY}(Nenhuma figura no album){c.RESET}")
    else:
        for rarity, count in stats["rarity_distribution"].items():
            color_prefix = getattr(c, rarity.name, c.WHITE)
            print(f"  {color_prefix}{rarity.name:<12}{c.RESET} : {count}x")

    print(f"\n{c.DARK_GRAY}------------------------------------------------{c.RESET}")

    print(f"{c.BOLD}Distribuição por Posicao:{c.RESET}")
    if not stats["position_distribution"]:
        print(f"  {c.DARK_GRAY}(Nenhuma figura no album){c.RESET}")
    else:
        for position, count in stats["position_distribution"].items():
            print(f"  {c.CYAN}{position.name:<5}{c.RESET} : {count}x")

    print(f"\n{c.DARK_GRAY}------------------------------------------------{c.RESET}")

    print(f"{c.BOLD}Figuras Repetidas em Detalhes:{c.RESET}")
    if not stats["duplicate_details"]:
        print(f"  {c.LIGHT_GRAY}Nenhuma figura repetida disponivel.{c.RESET}")
    else:
        for fig, dup_qty in stats["duplicate_details"].items():
            # Color-codes the player's name based on their specific card rarity
            rarity_color = getattr(c, fig.rarity.name, c.WHITE)
            print(
                f"  • {rarity_color}{fig.name:<20}{c.RESET} [ID {fig.id:02d}] : {c.RED}+{dup_qty} repetidas{c.RESET}"
            )

    print()
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY


def alb_display_repeated(album: FigurineAlbum) -> Screen:
    print_section_name_full("REPETIDAS")

    c = Colors

    repeated_cards: list[Figurine] = album.get_repeated()

    if not repeated_cards:
        print(f"  {c.LIGHT_GRAY}Você não possui nenhuma figurinha repetida.{c.RESET}")
        print(f"  {c.LIGHT_GRAY}Seu álbum esta livre de repetições!{c.RESET}")
    else:
        print(
            f"{c.BOLD}{c.DARK_GRAY}  {'ID':<4} {'Nome':<22} {'Raridade':<12} {'Quantidade'}{c.RESET}"
        )
        print(
            f"{c.DARK_GRAY}  ------------------------------------------------{c.RESET}"
        )

        registry = album.get_registry()

        for fig in repeated_cards:
            rarity_color = getattr(c, fig.rarity.name, c.WHITE)

            dup_qty = registry.get(fig.id, 1) - 1

            print(
                f"  {c.DARK_GRAY}{fig.id:02d}{c.RESET}  "
                f"{rarity_color}{fig.name:<22}{c.RESET} "
                f"{rarity_color}{fig.rarity.name:<12}{c.RESET} "
                f"{c.RED}+{dup_qty} repetidas{c.RESET}"
            )

    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY


def alb_propose_exchange(
    album1: FigurineAlbum, album2: FigurineAlbum, history: FigurineQueue
) -> Screen:
    print_section_name_full("Propor troca")
    print(centered_msg_full("Troque!"))
    print_section_end_full()

    c = Colors

    figs1: list[Figurine] = album1.get_figurines()
    figs2: list[Figurine] = album2.get_figurines()

    reg1: dict = album1.get_registry()
    reg2: dict = album2.get_registry()

    print(f"\n{c.BOLD}Suas Figurinhas:{c.RESET}")
    print(SEPARATOR)
    for fig in figs1:
        rarity_color = getattr(c, fig.rarity.name, c.WHITE)
        qtd_repeated = reg1.get(fig.id, 1) - 1
        txt_repetidas = (
            f" ({c.RED}+{qtd_repeated}{c.RESET})" if qtd_repeated > 0 else ""
        )
        print(f"  [{rarity_color}{fig.id:02d}{c.RESET}] {fig.name:<22}{txt_repetidas}")

    print(f"\n{c.BOLD}Figurinhas do oponente:{c.RESET}")
    print(SEPARATOR)
    for fig in figs2:
        rarity_color = getattr(c, fig.rarity.name, c.WHITE)
        qtd_repeated = reg2.get(fig.id, 1) - 1
        txt_repetidas = (
            f" ({c.RED}+{qtd_repeated}{c.RESET})" if qtd_repeated > 0 else ""
        )
        print(f"  [{rarity_color}{fig.id:02d}{c.RESET}] {fig.name:<22}{txt_repetidas}")

    print_section_end_full()

    transaction_ok: bool = True
    id_min = 0
    id_max = TOTAL_FIGURINES

    error_msg: str = (
        f"Formato inválido! Digite dois IDs separados por virgula entre {id_min} e {id_max}."
    )
    raw_input: str | None = get_and_validate_input(
        prompt="Digite os ids para a troca, no formato (seu_id,id_rival)",
        validator=lambda v: validate_exchange_format(v, id_min, id_max),
        error_msg=error_msg,
        cancel_key="B",
    )

    if raw_input is None:
        print(f"\n{c.YELLOW}Troca cancelada.{c.RESET}")
        return Screen.BACK

    parts: list[str] = raw_input.split(",")
    give_id: int = int(parts[0].strip())
    take_id: int = int(int(parts[1].strip()))

    give_fig: Figurine | None = album1.find_by_id(give_id)
    take_fig: Figurine | None = album2.find_by_id(take_id)

    error_msgs: list[str] = []

    if give_fig is None:
        error_msgs.append(
            format_error(f"Você não possui a figurinha com ID: {give_id}")
        )
        transaction_ok = False

    if take_fig is None:
        error_msgs.append(
            format_error(f"Oponente não possui a figurinha com ID: {take_id}")
        )
        transaction_ok = False

    if not (album1.propose_exchange(album2, give_fig, take_fig, history)):
        error_msgs.append(
            format_error(f"As figurinhas não são repetidas em seus respectivos álbuns")
        )
        transaction_ok = False

    if transaction_ok:
        print(f"\n{c.BOLD}{c.LIGHT_GREEN}TROCA REALIZADA COM SUCESSO!{c.RESET}")
    else:
        error_msgs.append(format_error(f"Transação não concluída"))

    [print(e) for e in error_msgs]

    print_section_end_full()

    print("\n[A] Tentar novamente")
    nav, choice = get_nav_input(False)
    if nav:
        return nav

    match choice:
        case "a":
            return Screen.STAY

    return Screen.BACK


def gen_save_data(
    album1: FigurineAlbum, album2: FigurineAlbum, history: FigurineQueue
) -> Screen:
    print_section_name_full("Salvar dados")

    confirm: str | None = get_and_validate_input(
        prompt="Deseja salvar todos os dados em CSV? (S/N)",
        validator=lambda v: v.upper() in ["S", "N"],
        error_msg="Entrada invalida. Digite S para Sim ou N para Não.",
        cancel_key="B",
    )

    if confirm is None or confirm.upper() == "N":
        return Screen.BACK

    all_ok: bool = True

    all_ok = album1.save_csv("album1.csv")
    all_ok = album2.save_csv("album2.csv")
    all_ok = history.save_csv("history.csv")

    if all_ok:
        print("Dados salvos com sucesso!\n")

    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY

def gen_load_data(
        album1: FigurineAlbum, album2: FigurineAlbum, history: FigurineQueue, fig_pool: FigurineExamples
) -> Screen:
    print_section_name_full("Carregar dados")

    confirm: str | None = get_and_validate_input(
        prompt="Deseja carregar todos os dados CSV? (S/N)",
        validator=lambda v: v.upper() in ["S", "N"],
        error_msg="Entrada invalida. Digite S para Sim ou N para Não.",
        cancel_key="B",
    )

    if confirm is None or confirm.upper() == "N":
        return Screen.BACK

    all_ok: bool = True

    all_ok = album1.load_csv("album1.csv", fig_pool)
    all_ok = album2.load_csv("album2.csv", fig_pool)
    all_ok = history.load_csv("history.csv", fig_pool)

    if all_ok:
        print("Dados carregados com sucesso!\n")

    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY

def hist_display(history: FigurineQueue) -> Screen:
    print_section_name_full("Histórico de transações")
    print()

    c = Colors
    history_records = history.get_history()

    try:
        term_width = os.get_terminal_size().columns
    except OSError:
        term_width = 80

    padding: int = max(0, (term_width - 56) // 2)
    p_space: str = " " * padding

    print_section_end_full(True, Colors.WHITE)

    if not history_records:
        print(centered_msg_full("Nenhuma troca foi realizada ainda.", c.DARK_GRAY, bold=False))
    else:
        print(f"{p_space}{c.BOLD}{c.DARK_GRAY}{'SAIU (Deixou a coleção)':<23}     {'ENTROU (Nova na coleção)'}{c.RESET}")
        print_section_end_full(True, Colors.WHITE)

        for _, (fig_out, fig_in) in enumerate(history_records, 1):
            cor_out = getattr(c, fig_out.rarity.name, c.WHITE)
            cor_in = getattr(c, fig_in.rarity.name, c.WHITE)
            
            print(
                f"{p_space}{c.RED}-{c.RESET} {cor_out}{fig_out.name:<21}{c.RESET} "
                f"{c.DARK_GRAY}--->{c.RESET} "
                f"{c.GREEN}+{c.RESET} {cor_in}{fig_in.name}{c.RESET}"
            )

    print_section_end_full(True, Colors.WHITE)

    print()
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY


def todo_screen() -> Screen:
    print_section_name_full("TODO")
    print(centered_msg_full("Screen yet to be implemented"))
    print_section_end_full()

    nav, _ = get_nav_input()
    if nav:
        return nav
    return Screen.STAY
