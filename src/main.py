from structs.Album import FigurineAlbum
from structs.Figurine import Figurine
from structs.Queue import FigurineQueue
from utils.types import FigurineRarity, FootballPosition


def main() -> int:
    history: FigurineQueue = FigurineQueue()
    album: FigurineAlbum = FigurineAlbum()

    f1: Figurine = Figurine(0, "test", "BRA", FootballPosition.CB, FigurineRarity.RARE)
    f2: Figurine = Figurine(
        1, "test2", "JAP", FootballPosition.RWB, FigurineRarity.LEGENDARY
    )
    f3: Figurine = Figurine(
        2, "testc", "BEL", FootballPosition.AM, FigurineRarity.COMMON
    )

    history.enqueue(f1)
    history.enqueue(f2)
    history.enqueue(f3)

    album.append(f1)
    album.append(f2)
    album.prepend(f3)

    print(album.find_by_id(1))
    print(album.find_by_name("testc"))
    [print(f) for f in album.find_by_country("BRA")]

    album.display_for_admin()
    album.display_cards()

    return 0


if __name__ == "__main__":
    main()
