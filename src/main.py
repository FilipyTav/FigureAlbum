from structs.Album import FigurineAlbum
from structs.Figurine import Figurine
from structs.Queue import FigurineQueue
from utils.figurine_examples import FigurineExamples
from utils.types import FigurineRarity, FootballPosition


def main() -> int:
    examples: FigurineExamples = FigurineExamples()

    history: FigurineQueue = FigurineQueue()

    album: FigurineAlbum = FigurineAlbum()
    album2: FigurineAlbum = FigurineAlbum()

    # history.enqueue(f1)
    # history.enqueue(f2)
    # history.enqueue(f3)

    album.append(examples.get(0))
    album.append(examples.get(1))
    album.prepend(examples.get(2))
    album.append(examples.get(1))

    # print(album.find_by_id(1))
    # print(album.find_by_name("testc"))
    # [print(f) for f in album.find_by_country("BRA")]

    [print(r) for r in album.get_repeated()]
    album.display_for_admin()
    album.display_cards()

    return 0


if __name__ == "__main__":
    main()
