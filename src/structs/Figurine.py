from __future__ import annotations

from utils.colors import Colors
from utils.strings import SEPARATOR_WIDTH, get_visible_len, truncate_string
from utils.types import FigurineRarity, FootballPosition


class Figurine:
    def __init__(
        self,
        id: int,
        name: str,
        country: str,
        position: FootballPosition,
        rarity: FigurineRarity,
    ) -> None:
        self.id: int = id
        self.name: str = name
        self.country: str = country
        self.position: FootballPosition = position
        self.rarity: FigurineRarity = rarity

    def display_as_card(
        self, position_counter: int = 1, content_width: int = SEPARATOR_WIDTH - 4
    ) -> None:
        pos_str: str = self.position.full_name if self.position else "N/A"
        rarity_str: str = self.rarity.display_name if self.rarity else "N/A"

        # Dynamic badge based on position
        if position_counter == 1:
            status_badge = (
                f"{Colors.BG_GREEN}{Colors.BLACK}{Colors.BOLD} NEXT UP {Colors.RESET}"
            )
        else:
            status_badge = (
                f"{Colors.DARK_GRAY}#{position_counter} in line{Colors.RESET}"
            )

        # 1. Row: Status Badge
        badge_padding: int = content_width + (
            len(status_badge) - get_visible_len(status_badge)
        )
        row_badge = f"│ {status_badge:<{badge_padding}} │"

        # 2. Row: Name and ID
        name_part: str = f"{Colors.BOLD}{truncate_string(self.name, 20)}{Colors.RESET}"
        id_part: str = f"ID: #{self.id}"
        combined_name_id: str = (
            f"{name_part:<{20 + (len(name_part) - get_visible_len(name_part))}} {id_part:>20}"
        )
        row_name: str = (
            f"│ {combined_name_id:<{content_width + (len(combined_name_id) - get_visible_len(combined_name_id))}} │"
        )

        # 3. Row: Country
        country_str: str = f"{self.country}"
        row_country: str = f"│ {country_str:<{content_width}} │"

        # 4. Row: Position
        full_pos_str: str = f"Position: {pos_str}"
        row_pos: str = (
            f"│ {truncate_string(full_pos_str, content_width):<{content_width}} │"
        )

        # 5. Row: Rarity
        rarity_part: str = (
            f"{self.rarity.bgcolor}{Colors.BLACK}  {Colors.BOLD}{rarity_str}  {Colors.RESET}"
        )
        full_rarity_str: str = f"Rarity:   {rarity_part}"
        rarity_padding = content_width + (
            len(full_rarity_str) - get_visible_len(full_rarity_str)
        )
        row_rarity: str = f"│ {full_rarity_str:<{rarity_padding}} │"

        # --- PRINT CARD BLOCKS ---
        print("┌" + "─" * (SEPARATOR_WIDTH - 2) + "┐")
        print(row_badge)
        print("│" + " " * (SEPARATOR_WIDTH - 2) + "│")
        print(row_name)
        print(row_country)
        print("│" + " " * (SEPARATOR_WIDTH - 2) + "│")
        print(row_pos)
        print(row_rarity)
        print("└" + "─" * (SEPARATOR_WIDTH - 2) + "┘\n")

    def display_for_admin(
        self, position_counter: int = 1, content_width: int = SEPARATOR_WIDTH - 4
    ) -> None:
        pos_str: str = self.position.full_name if self.position else "N/A"
        rarity_str: str = self.rarity.display_name if self.rarity else "N/A"

        print(
            f"#{position_counter:<18} | "
            f"{self.id:<6} | "
            f"{truncate_string(self.name, 20):<20} | "
            f"{self.country:<15} | "
            f"{pos_str:<20} | "
            f"{self.rarity.fgcolor}{Colors.BOLD}{rarity_str:<12}{Colors.RESET}"
        )

    def __str__(self) -> str:
        pos: str = self.position.name if self.position else "N/A"

        if self.rarity:
            badge: str = (
                f"{self.rarity.fgcolor}{Colors.BOLD}{self.rarity.display_name.upper()}{Colors.RESET}"
            )
        else:
            badge: str = "[N/A]"

        return f"#{self.id} {self.name} ({self.country}) — {pos} * {badge}"


class SFigurineNode:
    def __init__(self, data: Figurine, next: SFigurineNode | None = None) -> None:
        self.next: SFigurineNode | None = next
        self.data: Figurine | None = data
