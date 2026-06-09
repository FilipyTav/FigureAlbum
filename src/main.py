from structs.Figurine import Figurine
from structs.Queue import FigurineQueue
from utils.types import FigurineRarity, FootballPosition


def main() -> int:
    q: FigurineQueue = FigurineQueue()
    f1: Figurine = Figurine(0, "test", "BRA", FootballPosition.CB, FigurineRarity.RARE)
    q.enqueue(f1)
    q.display_for_admin()
    q.dequeue()
    return 0


if __name__ == "__main__":
    main()
