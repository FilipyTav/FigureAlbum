import csv
import pathlib
from structs.Figurine import Figurine, SFigurineNode
from utils.colors import Colors
from utils.config import DATA_DIR
from utils.figurine_examples import FigurineExamples
from utils.strings import (
    SEPARATOR,
    SEPARATOR_WIDTH,
    centered_msg,
    format_error,
    print_centered_header,
    print_section_name,
    print_section_name_full,
    truncate_string,
)


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
                fig.display_for_admin(position_counter)
            else:
                print(
                    f"#{position_counter:<18} | [ERROR: Corrupted Node - Missing Data]"
                )

            current = current.next
            position_counter += 1

        print(f"\nTotal in Queue: {position_counter - 1}")
        print(SEPARATOR)

    def display_cards(self) -> None:
        """Display all figurines."""
        print(SEPARATOR)
        print(f"{Colors.BOLD}FIGURINE COLLECTION QUEUE{Colors.RESET}\n")

        if self.__head is None:
            print("Queue is currently empty!")
            print(SEPARATOR)
            return

        current: SFigurineNode | None = self.__head
        position_counter: int = 1

        while current is not None:
            if current.data is not None:
                current.data.display_as_card(position_counter)
            else:
                print(f"[Position #{position_counter}] Item temporarily unavailable.\n")

            current = current.next
            position_counter += 1

        print(f"Total items: {Colors.BOLD}{position_counter - 1}{Colors.RESET}")
        print(SEPARATOR)

    def get_history(self) -> list[tuple[Figurine, Figurine]]:
        """Returns (fig_out, fig_in)"""
        current: SFigurineNode | None = self.__head
        history_list: list[tuple[Figurine, Figurine]] = []

        if not current:
            return history_list

        while current and current.next:
            card_out: Figurine | None = current.data
            card_in: Figurine | None = current.next.data

            if card_out is not None and card_in is not None:
                history_list.append((card_out, card_in))

            if current.next:
                current = current.next.next
            else:
                current = current.next

        return history_list

    def save_csv(self, filepath: pathlib.Path = DATA_DIR / "data.csv") -> bool:
        try:
            with open(filepath, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerow(["id", "name", "country", "position", "rarity"])

                current = self.__head
                while current is not None:
                    fig: Figurine | None = current.data
                    assert fig

                    writer.writerow(
                        [
                            fig.id,
                            fig.name,
                            fig.country,
                            fig.position.name,
                            fig.rarity.name,
                        ]
                    )

                    current = current.next

            print(
                f" {Colors.LIGHT_GREEN}{Colors.RESET} History successfully saved to '{Colors.UNDERLINE}{filepath}{Colors.RESET}'."
            )
        except IOError as e:
            print(format_error(f"Could not save album data to {filepath}. ({e})"))
            return False

        return True

    def load_csv(self, filepath: pathlib.Path, examples: FigurineExamples) -> bool:
        if not filepath.exists():
            return False

        try:
            with open(filepath, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    id, name, country, position, rarity = row
                    fig: Figurine | None = examples.get(int(id))
                    if fig:
                        self.enqueue(fig)

        except IOError as e:
            print(format_error(f"Could not load history data from {filepath}. ({e})"))
            return False

        except ValueError:
            print(format_error(f"Malformatted row data in file {filepath}."))
            return False

        return True
