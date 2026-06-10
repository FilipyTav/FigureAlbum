from structs.MenuStack import MenuStack

from ui.screen_manager import (
    alb_add_fig,
    alb_display,
    alb_display_repeated,
    alb_display_stats,
    alb_find_fig,
    alb_propose_exchange,
    alb_rm_fig,
    main_menu,
    screen_clear,
    todo_screen,
)
from ui.state import AppState
from utils.strings import format_error
from utils.types import Screen, ScreenConfig


class MenuManager:
    def __init__(self, state: AppState):
        self.__screen_history: MenuStack = MenuStack()

        self.__is_running: bool = True
        self.__screen_history.push(Screen.MAIN)

        self.state: AppState = state
        self.registry: list[ScreenConfig] = [
            # Main
            # ------------
            ScreenConfig(Screen.MAIN, "Menu Inicial", main_menu, None),
            # ------------
            # Children of MAIN
            # ------------
            ScreenConfig(
                Screen.ALBUM_ADD,
                "Adicionar figuinha",
                lambda: alb_add_fig(self.state.user_album, self.state.figurine_pool),
                Screen.MAIN,
            ),
            ScreenConfig(
                Screen.ALBUM_REMOVE,
                "Remover figuinha",
                lambda: alb_rm_fig(self.state.user_album),
                Screen.MAIN,
            ),
            ScreenConfig(
                Screen.ALBUM_FIND,
                "Consultar figurinha",
                lambda: alb_find_fig(self.state.user_album),
                Screen.MAIN,
            ),
            ScreenConfig(
                Screen.ALBUM_DISPLAY,
                "Mostrar Álbum",
                lambda: alb_display(self.state.user_album),
                Screen.MAIN,
            ),
            ScreenConfig(
                Screen.ALBUM_STATS,
                "Estatísticas Álbum",
                lambda: alb_display_stats(
                    self.state.user_album, self.state.figurine_pool
                ),
                Screen.MAIN,
            ),
            ScreenConfig(
                Screen.ALBUM_SHOW_REPEATED,
                "Mostrar repetidas",
                lambda: alb_display_repeated(self.state.user_album),
                Screen.MAIN,
            ),
            ScreenConfig(
                Screen.ALBUM_EXCHANGE,
                "Fazer troca",
                lambda: alb_propose_exchange(
                    self.state.user_album, self.state.rival_album, self.state.history
                ),
                Screen.MAIN,
            ),
            # fmt: off
            ScreenConfig(Screen.SAVE_DATA, "Salvar dados", todo_screen, Screen.MAIN),
            ScreenConfig(Screen.LOAD_DATA, "Carregar dados", todo_screen, Screen.MAIN),
            # ------------
            # Placeholder
            # ------------
            ScreenConfig(Screen.TODO, "(Em breve)", todo_screen, None),
            # ------------
            # fmt: on
        ]
        self._dispatch_map = {config.id: config.handler for config in self.registry}

    def run(self):
        screen: Screen | None = None
        new_sc: Screen = Screen.MAIN

        while self.__is_running and not self.__screen_history.is_empty():
            screen = self.__screen_history.peek()
            if not screen:
                break

            screen_clear()
            # self.__screen_history.print_stack()
            new_sc = self._handle_nav(screen)

            self._navigate(screen, new_sc)

    def _handle_nav(self, screen: Screen) -> Screen:
        """Lookup and execute the handler for the given screen"""

        handler = self._dispatch_map.get(screen)

        if screen == Screen.MAIN:
            return handler(self.registry)  # type: ignore

        return handler()  # type: ignore

    def _navigate(self, current_sc: Screen, new_sc: Screen) -> None:
        if new_sc == current_sc or new_sc == Screen.STAY:
            return

        if new_sc == Screen.MAIN:
            self.__screen_history.clear()
            self.__screen_history.push(Screen.MAIN)

        elif new_sc == Screen.EXIT:
            print("\nEncerrando o sistema...")
            self.__is_running = False
            self.__screen_history.clear()

        elif new_sc == Screen.BACK:
            self.__screen_history.pop()

        else:
            self.__screen_history.push(new_sc)
