from structs.Figurine import Figurine, SFigurineNode
from utils.colors import Colors
from utils.strings import SEPARATOR, truncate_string


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
