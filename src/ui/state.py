from dataclasses import dataclass

from structs.Album import FigurineAlbum
from structs.Queue import FigurineQueue


@dataclass
class AppState:
    user_album: FigurineAlbum
    rival_album: FigurineAlbum
    history: FigurineQueue
