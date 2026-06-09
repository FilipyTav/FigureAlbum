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

    history.enqueue(examples.get(0))
    history.enqueue(examples.get(1))
    history.enqueue(examples.get(2))
    history.enqueue(examples.get(2))
    a = history.get_history()
    print(a)

    album.append(examples.get(0))
    album.append(examples.get(1))
    album.prepend(examples.get(2))
    album.append(examples.get(1))

    album2.append(examples.get(3))
    album2.append(examples.get(5))
    album2.prepend(examples.get(5))
    album2.append(examples.get(7))

    # print(album.find_by_id(1))
    # print(album.find_by_name("testc"))
    # [print(f) for f in album.find_by_country("BRA")]
    # album.propose_exchange(album2, examples.get(1))

    # album.display_for_admin()
    # [print(r) for r in album.get_repeated()]
    #
    # print()
    # album2.display_for_admin()
    # [print(r) for r in album2.get_repeated()]
    # print()
    #
    # print(album.is_repeated(1))
    # print(album2.is_repeated(5))
    # print(
    #     album.propose_exchange(
    #         album2, give_fig=examples.get(1), take_fig=examples.get(5)
    #     )
    # )
    #
    # album.display_for_admin()
    # [print(r) for r in album.get_repeated()]
    #
    # print()
    # album2.display_for_admin()
    # [print(r) for r in album2.get_repeated()]
    # print()

    return 0


if __name__ == "__main__":
    main()
