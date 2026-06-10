from structs.Album import FigurineAlbum
from structs.Figurine import Figurine
from structs.Menu import MenuManager
from structs.Queue import FigurineQueue
from ui.state import AppState
from utils.config import DATA_DIR
from utils.figurine_examples import FigurineExamples
from utils.types import FigurineRarity, FootballPosition


def main() -> int:
    examples: FigurineExamples = FigurineExamples()

    history: FigurineQueue = FigurineQueue()

    album: FigurineAlbum = FigurineAlbum()
    album2: FigurineAlbum = FigurineAlbum()

    # album.append(examples.get(0))
    # album.append(examples.get(1))
    # album.prepend(examples.get(2))
    # album.append(examples.get(1))
    #
    # album2.append(examples.get(3))
    # album2.append(examples.get(5))
    # album2.prepend(examples.get(5))
    # album2.append(examples.get(7))

    menu: MenuManager = MenuManager(AppState(album, album2, history, examples))
    menu.run()

    # history.enqueue(examples.get(0))
    # history.enqueue(examples.get(2))
    # history.enqueue(examples.get(4))
    # history.enqueue(examples.get(0))

    return 0


if __name__ == "__main__":
    main()
