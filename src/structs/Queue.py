from structs.Figurine import Figurine, SFigurineNode


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

    def display_for_admin(self):
        """Visual chain"""
        if self.is_empty():
            print("\nEmpty Queue.")
            return

        print(f"\n--- Figurine Queue ({self.len()}) ---")

        current = self.__head
        chain = []

        while current:
            chain.append(f"[{current.data.name}]")
            current = current.next

        visual_chain = " ⇄ ".join(chain)

        print(f"HEAD ➔ {visual_chain} ➔ TAIL")
        print("-" * 40)
