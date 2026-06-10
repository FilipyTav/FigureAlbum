from dataclasses import dataclass

from structs.Album import FigurineAlbum
from structs.Queue import FigurineQueue
from utils.figurine_examples import FigurineExamples


@dataclass
class AppState:
    user_album: FigurineAlbum
    rival_album: FigurineAlbum
    history: FigurineQueue
    figurine_pool: FigurineExamples
