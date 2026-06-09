from structs.Figurine import Figurine, SFigurineNode
from utils.colors import Colors
from utils.strings import (
    SEPARATOR,
    SEPARATOR_WIDTH,
    centered_msg,
    clean_string,
    format_error,
    print_section_name,
    truncate_string,
)


class FigurineAlbum:
    def __init__(self):
        self.__head: SFigurineNode | None = None
        self.__tail: SFigurineNode | None = None
        self.__count: int = 0

        # Avoids repetition
        self.__registered: dict[str, set[str]] = {}

    def insert_at(self, pos: int, data: Figurine) -> bool:
        """Insert at pos"""
        if pos < 0 or pos > self.__count:
            print(f"Index out of range: {pos}, the list has {self.__count} element(s)")
            return False

        new_node: SFigurineNode = SFigurineNode(data)

        # Empty
        if self.is_empty():
            self.__head = self.__tail = new_node

        # new_node is now the head
        elif pos == 0:
            new_node.next = self.__head

            self.__head = new_node
        # new_node is now the tail
        elif pos == self.__count:
            if self.__tail:
                self.__tail.next = new_node
            self.__tail = new_node
        else:
            current: SFigurineNode | None = self.__head

            for _ in range(pos - 1):
                if not current:
                    return False
                current = current.next

            # Because LSP
            assert current is not None
            assert current.next is not None

            new_node.next = current.next
            current.next = new_node

        self.__count += 1
        return True

    def is_empty(self) -> bool:
        return not (self.__head and self.__tail)

    def len(self) -> int:
        return self.__count

    def append(self, f: Figurine) -> bool:
        """Add to end"""
        return self.insert_at(self.len(), f)

    def prepend(self, f: Figurine) -> bool:
        """Add to start"""
        return self.insert_at(0, f)

    def find_by_name(self, name: str) -> Figurine | None:
        if self.is_empty():
            print("Lista vazia.")
            return None

        current: SFigurineNode | None = self.__head
        while current:
            if clean_string(current.data.name) == clean_string(name):  # type: ignore
                return current.data

            current = current.next

        return None

    def find_by_id(self, id: int) -> Figurine | None:
        if self.is_empty() or id < 0:
            return None

        current: SFigurineNode | None = self.__head
        while current:
            if current.data.id == id:  # type: ignore
                return current.data

            current = current.next

        return None

    def remove_at(self, pos: int) -> bool:
        """Remove at pos"""
        if pos < 0 or pos >= self.__count:
            print(f"Index out of range: {pos}, the list has {self.__count} element(s)")
            return False

        if self.is_empty():
            return False

        if pos == 0:
            self.__head = self.__head.next  # type: ignore
            self.__count -= 1
            return True

        current: SFigurineNode | None = self.__head
        index: int = 0
        while current:
            if index + 1 == pos:
                assert current.next
                current.next = current.next.next
                self.__count -= 1
                return True

            current = current.next
            index += 1

        return False

    def remove_by_id(self, id: int) -> bool:
        """Remove figurine by id"""
        if id < 0 or self.is_empty():
            return False

        assert self.__head

        # Removes the head
        if self.__head.data.id == id:  # type: ignore
            fig = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1

            if self.__count == 0:
                self.__tail = None

            return True

        current: SFigurineNode | None = self.__head
        index: int = 0
        # Avoids searching tail
        while current and current.next:
            if current.next.data.id == id:  # type: ignore
                fig = current.next.data
                node_to_remove: SFigurineNode = current.next

                if node_to_remove == self.__tail:
                    self.__tail = current

                current.next = node_to_remove.next

                self.__count -= 1
                return True

            current = current.next
            index += 1

        return False

    def __str__(self) -> str:
        return f"FigurineAlbum(Size: {self.__count}, Head: {self.__head.data.name if self.__head else 'None'})"  # type: ignore

    def display_for_admin(self) -> None:
        """Prints a formatted tabular view of the figurines for administrators."""
        print(SEPARATOR)
        print("Figurine Album (ADMIN VIEW)\n")
        if self.__head is None:
            print("Album is currently EMPTY.")
            print(SEPARATOR)
            return

        # Headers
        print(
            f"{'Position in Album':<19} | {'ID':<6} | {'Name':<20} | {'Country':<15} | {'Field Position':<20} | {'Rarity':<12}"
        )
        print("-" * 103)

        current = self.__head
        position_counter = 1

        while current is not None:
            if current.data is not None:
                fig: Figurine = current.data
                fig.display_for_admin()
            else:
                print(
                    f"#{position_counter:<18} | [ERROR: Corrupted Node - Missing Data]"
                )

            current = current.next
            position_counter += 1

        print(f"\nTotal in Album: {position_counter - 1}")
        print(SEPARATOR)

    def display_cards(self) -> None:
        """Display all figurines."""
        print(SEPARATOR)
        print(f"{Colors.BOLD}FIGURINE ALBUM{Colors.RESET}\n")

        if self.__head is None:
            print("Album is currently empty!")
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

    def get_statistics(self) -> None:
        pass
