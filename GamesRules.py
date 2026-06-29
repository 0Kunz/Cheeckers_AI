from CellCode import CellCode

class GamesRules:
    ONE_CELL = 1

    DIAGONAL_DIRECTIONS = [
        (-ONE_CELL, -ONE_CELL),  # cima esquerda
        (-ONE_CELL, ONE_CELL),  # cima direita
        (ONE_CELL, -ONE_CELL),  # baixo esquerda
        (ONE_CELL, ONE_CELL),  # baixo direita
    ]

    def __init__(self, board_map):
        self.board_map = board_map

    def get_valid_moves(self, men_position):
        valid_moves = []
        men_row, men_column = men_position
        for row_direction, column_direction in self.DIAGONAL_DIRECTIONS:
            target_row = men_row + row_direction
            target_column = men_column + column_direction
            target_position = (target_row, target_column)

            if self.is_out_of_bounds(target_position):
                continue

            cell = self.board_map[target_position]

            if CellCode.is_empty_playable(cell):
                valid_moves.append(target_position)

        return valid_moves

    def is_out_of_bounds(self, position):
        row, column = position
        total_rows, total_columns = self.board_map.shape

        return (
                row < 0
                or row >= total_rows
                or column < 0
                or column >= total_columns
        )