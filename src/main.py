from structs.Figurine import Figurine
from structs.Queue import FigurineQueue
from utils.types import FigurineRarity, FootballPosition


def main() -> int:
    history: FigurineQueue = FigurineQueue()
    f1: Figurine = Figurine(0, "test", "BRA", FootballPosition.CB, FigurineRarity.RARE)
    history.enqueue(f1)
    history.enqueue(f1)
    history.display_for_admin()
    history.display_for_user()
    history.dequeue()
    history.dequeue()
    return 0


if __name__ == "__main__":
    main()
