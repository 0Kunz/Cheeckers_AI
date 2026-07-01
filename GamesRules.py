from CellCode import CellCode

class GamesRules:
    ONE_CELL = 1
    TWO_CELLS = 2

    DIAGONAL_DIRECTIONS = [
        (-ONE_CELL, -ONE_CELL),  # cima esquerda
        (-ONE_CELL, ONE_CELL),  # cima direita
        (ONE_CELL, -ONE_CELL),  # baixo esquerda
        (ONE_CELL, ONE_CELL),  # baixo direita
    ]

    def __init__(self, board_map):
        self.board_map = board_map

    def get_valid_moves(self, men_position, valid_moves=None, is_recursive=False):
        if None == valid_moves:
            valid_moves = { 'landing': [], 'captured': [], 'basic_moves': [] }
        else:
            is_recursive = True


        men_row, men_column = men_position
        men_code = self.get_cell_code(men_position).normal_version()

        for row_direction, column_direction in self.DIAGONAL_DIRECTIONS:
            target_position = (
                men_row + row_direction,
                men_column + column_direction
            )

            if self.is_out_of_bounds(target_position):
                continue

            cell = self.get_cell_code(target_position).normal_version()

            if self.is_opposite_piece(cell, men_code):
                enemy_position = (
                    men_row + row_direction,
                    men_column + column_direction
                )

                landing_position = (
                    men_row + (row_direction * self.TWO_CELLS),
                    men_column + (column_direction * self.TWO_CELLS)
                )

                men_code = self.get_cell_code(landing_position)

                if men_code.is_empty_playable():
                    valid_moves['landing'].append(landing_position)
                    valid_moves['captured'].append(enemy_position)
                    self.get_valid_moves(landing_position, valid_moves)

            if CellCode.is_empty_playable(cell) and not is_recursive :
                valid_moves['basic_moves'].append(target_position)

        return valid_moves

    @staticmethod
    def is_opposite_piece(cell_code, men_code):
        if not cell_code.is_piece():
            return False

        if not men_code.is_piece():
            return False

        return cell_code.is_black_piece() != men_code.is_black_piece()


    def is_out_of_bounds(self, position):
        row, column = position
        total_rows, total_columns = self.board_map.shape

        return (
                row < 0
                or row >= total_rows
                or column < 0
                or column >= total_columns
        )

    def get_cell_code(self, position, board_map=None):
        if board_map is None:
            board_map = self.board_map

        row, column = position

        return CellCode(board_map[row, column])