from structs.Figurine import Figurine, SFigurineNode
from utils.colors import Colors
from utils.strings import SEPARATOR, SEPARATOR_WIDTH, get_visible_len, truncate_string


class FigurineQueue:
    def __init__(self):
        self.__head: SFigurineNode | None = None
        self.__tail: SFigurineNode | None = None
        self.__count: int = 0

    def enqueue(self, f: Figurine) -> bool:
        new_node: SFigurineNode = SFigurineNode(f)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
        else:
            assert self.__tail
            self.__tail.next = new_node

            self.__tail = new_node

        self.__count += 1
        return True

    def dequeue(self) -> Figurine | None:
        if self.is_empty():
            return None

        assert self.__head
        fig: Figurine | None = self.__head.data

        self.__head = self.__head.next

        if not self.__head:
            self.__tail = None

        self.__count -= 1
        return fig

    def peek(self) -> Figurine | None:
        if self.is_empty():
            return None

        return self.__head.data  # type: ignore

    def is_empty(self) -> bool:
        return not (self.__head and self.__tail)

    def len(self) -> int:
        return self.__count

    def clear(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    def __str__(self) -> str:
        return f"Figurine Queue(Size: {self.len()}, Head: {self.__head.data.name if self.__head else 'None'})"  # type: ignore

    def display_for_admin(self) -> None:
        """Prints a formatted tabular view of the queue for administrators."""
        print(SEPARATOR)
        print("Figurine Queue (ADMIN VIEW)\n")
        if self.__head is None:
            print("Queue is currently EMPTY.")
            print(SEPARATOR)
            return

        # Headers
        print(
            f"{'Position in Queue':<19} | {'ID':<6} | {'Name':<20} | {'Country':<15} | {'Field Position':<20} | {'Rarity':<12}"
        )
        print("-" * 103)

        current = self.__head
        position_counter = 1

        while current is not None:
            if current.data is not None:
                fig: Figurine = current.data

                pos_str: str = fig.position.full_name if fig.position else "N/A"
                rarity_str: str = fig.rarity.display_name if fig.rarity else "N/A"

                # Print the row with clean alignment
                print(
                    f"#{position_counter:<18} | "
                    f"{fig.id:<6} | "
                    f"{truncate_string(fig.name, 20):<20} | "
                    f"{fig.country:<15} | "
                    f"{pos_str:<20} | "
                    f"{fig.rarity.color}{rarity_str:<12}{Colors.RESET}"
                )
            else:
                print(
                    f"#{position_counter:<18} | [ERROR: Corrupted Node - Missing Data]"
                )

            current = current.next
            position_counter += 1

        print(f"\nTotal in Queue: {position_counter - 1}n")
        print(SEPARATOR)

    def display_for_user(self) -> None:
        """Card view"""
        print(SEPARATOR)
        print(f"{Colors.BOLD}FIGURINE COLLECTION QUEUE{Colors.RESET}\n")

        if self.__head is None:
            print("Queue is currently empty!")
            print(SEPARATOR)
            return

        current: SFigurineNode | None = self.__head
        position_counter: int = 1

        # 4 for borders
        content_width: int = SEPARATOR_WIDTH - 4

        while current is not None:
            if current.data is not None:
                fig: Figurine = current.data

                pos_str: str = fig.position.full_name if fig.position else "N/A"
                rarity_str: str = fig.rarity.display_name if fig.rarity else "N/A"

                if position_counter == 1:
                    status_badge = f"{Colors.BG_GREEN}{Colors.BLACK}{Colors.BOLD} NEXT UP {Colors.RESET}"
                else:
                    status_badge = (
                        f"{Colors.DARK_GRAY}#{position_counter} in line{Colors.RESET}"
                    )

                badge_padding: int = content_width + (
                    len(status_badge) - get_visible_len(status_badge)
                )
                row_badge = f"│ {status_badge:<{badge_padding}} │"

                name_part = (
                    f"{Colors.BOLD}{truncate_string(fig.name, 20)}{Colors.RESET}"
                )
                id_part: str = f"ID: #{fig.id}"
                combined_name_id: str = (
                    f"{name_part:<{20 + (len(name_part) - get_visible_len(name_part))}} {id_part:>20}"
                )
                row_name: str = (
                    f"│ {combined_name_id:<{content_width + (len(combined_name_id) - get_visible_len(combined_name_id))}} │"
                )

                country_str: str = f"{fig.country}"
                row_country: str = f"│ {country_str:<{content_width}} │"

                full_pos_str: str = f"Position: {pos_str}"
                row_pos: str = f"│ {full_pos_str:<{content_width}} │"

                rarity_part: str = f"{fig.rarity.color}{rarity_str}{Colors.RESET}"
                full_rarity_str: str = f"Rarity:   {rarity_part}"
                rarity_padding = content_width + (
                    len(full_rarity_str) - get_visible_len(full_rarity_str)
                )
                row_rarity: str = f"│ {full_rarity_str:<{rarity_padding}} │"

                # --- CARD ---
                print("┌" + "─" * (SEPARATOR_WIDTH - 2) + "┐")
                print(row_badge)
                print("│" + " " * (SEPARATOR_WIDTH - 2) + "│")
                print(row_name)
                print(row_country)
                print("│" + " " * (SEPARATOR_WIDTH - 2) + "│")
                print(row_pos)
                print(row_rarity)
                print("└" + "─" * (SEPARATOR_WIDTH - 2) + "┘\n")
            else:
                print(f"[Position #{position_counter}] Item temporarily unavailable.\n")

            current = current.next
            position_counter += 1

        print(f"Total items: {Colors.BOLD}{position_counter - 1}{Colors.RESET}")
        print(SEPARATOR)
