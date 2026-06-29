import numpy as np
from GamesRules import GamesRules
from CellCode import CellCode

class GameManager:

    BLACK_PLAYER = "BLACK"
    RED_PLAYER = "RED"

    SELECTED_BY_NORMAL_MEN = {
        CellCode.BLACK_MEN: CellCode.BLACK_MEN_SELECTED,
        CellCode.RED_MEN: CellCode.RED_MEN_SELECTED,
    }

    NORMAL_BY_SELECTED_MEN = {
        CellCode.BLACK_MEN_SELECTED: CellCode.BLACK_MEN,
        CellCode.RED_MEN_SELECTED: CellCode.RED_MEN,
    }

    PLAYER_PIECES = {
        BLACK_PLAYER: {
            CellCode.BLACK_MEN,
            CellCode.BLACK_MEN_SELECTED,
            CellCode.BLACK_KING,
        },
        RED_PLAYER: {
            CellCode.RED_MEN,
            CellCode.RED_MEN_SELECTED,
            CellCode.RED_KING,
        },
    }

    N = CellCode.NOT_PLAYABLE
    E = CellCode.EMPTY_PLAYABLE
    R = CellCode.RED_MEN
    B = CellCode.BLACK_MEN

    INITIAL_BOARD_MAP = np.array([
        [N, R, N, R, N, R, N, R],
        [R, N, R, N, R, N, R, N],
        [N, R, N, R, N, R, N, R],
        [E, N, E, N, E, N, E, N],
        [N, E, N, E, N, E, N, E],
        [B, N, B, N, B, N, B, N],
        [N, B, N, B, N, B, N, B],
        [B, N, B, N, B, N, B, N],
    ], dtype=np.uint8)

    def __init__(self, board_coordinates):
        self.board_map = self.INITIAL_BOARD_MAP.copy()
        self.board_coordinates = board_coordinates
        self.games_rules = GamesRules(self.board_map)

        self.current_player = self.BLACK_PLAYER
        self.men_selected = None

    def click(self, x, y):
        clicked_position = self.get_clicked_position(x, y)

        if clicked_position is None:
            return

        if self.has_men_selected():
            self.handle_click_with_selected_men(clicked_position)
            return

        if self.is_current_player_piece(clicked_position):
            self.select_men(clicked_position)

    def handle_click_with_selected_men(self, clicked_position):
        if clicked_position == self.men_selected:
            self.unselect_men()
            return

        valid_moves = self.games_rules.get_valid_moves(self.men_selected)

        if clicked_position in valid_moves:
            self.move_selected_men_to(clicked_position)
            self.switch_player()
            return

        if self.is_current_player_piece(clicked_position):
            self.change_selected_men(clicked_position)
            return

        self.unselect_men()

    def move_selected_men_to(self, new_position):
        selected_position = self.men_selected
        selected_men_code = self.get_element(selected_position)

        normal_men_code = selected_men_code.normal_version()
        final_men_code = self.promote_men_if_needed(normal_men_code, new_position)

        self.set_element(selected_position, CellCode.EMPTY_PLAYABLE)
        self.set_element(new_position, final_men_code)

        self.men_selected = None

    def promote_men_if_needed(self, men_code, position):
        row, _ = position

        if men_code == CellCode.BLACK_MEN and row == 0:
            return CellCode.BLACK_KING

        if men_code == CellCode.RED_MEN and row == 7:
            return CellCode.RED_KING

        return men_code

    def change_selected_men(self, new_position):
        self.unselect_men()
        self.select_men(new_position)

    def select_men(self, position):
        men_code = self.get_element(position)
        selected_men_code = men_code.selected_version()

        if selected_men_code == men_code:
            return

        self.set_element(position, selected_men_code)
        self.men_selected = position

    def unselect_men(self):
        if self.men_selected is None:
            return

        selected_men_code = self.get_element(self.men_selected)
        normal_men_code = selected_men_code.normal_version()

        self.set_element(self.men_selected, normal_men_code)
        self.men_selected = None

    def has_men_selected(self):
        return self.men_selected is not None

    def is_current_player_piece(self, position):
        cell_code = self.get_element(position)

        if self.current_player == self.BLACK_PLAYER:
            return cell_code.is_black_piece()

        if self.current_player == self.RED_PLAYER:
            return cell_code.is_red_piece()

        return False

    def switch_player(self):
        if self.current_player == self.BLACK_PLAYER:
            self.current_player = self.RED_PLAYER
        else:
            self.current_player = self.BLACK_PLAYER

    def get_clicked_position(self, x, y):
        position = self.board_coordinates.get_tile_by_pixel(x, y)

        if position is None:
            return None

        return tuple(position)

    def get_board_map(self):
        return self.board_map

    def get_element(self, position):
        row, column = position
        return CellCode(self.board_map[row, column])

    def set_element(self, position, cell_code):
        row, column = position
        self.board_map[row, column] = cell_code