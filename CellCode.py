from enum import IntEnum

class CellCode(IntEnum):
    NOT_PLAYABLE = 0
    EMPTY_PLAYABLE = 1

    RED_MEN = 66
    RED_MEN_SELECTED = 67
    RED_KING = 68
    RED_KING_SELECTED = 69

    BLACK_MEN = 96
    BLACK_MEN_SELECTED = 97
    BLACK_KING = 98
    BLACK_KING_SELECTED = 99

    def is_empty_playable(self):
        return self == CellCode.EMPTY_PLAYABLE

    def is_piece(self):
        return self in (
            CellCode.RED_MEN,
            CellCode.RED_MEN_SELECTED,
            CellCode.RED_KING,
            CellCode.RED_KING_SELECTED,
            CellCode.BLACK_MEN,
            CellCode.BLACK_MEN_SELECTED,
            CellCode.BLACK_KING,
            CellCode.BLACK_KING_SELECTED,
        )

    def is_red_piece(self):
        return self in (
            CellCode.RED_MEN,
            CellCode.RED_MEN_SELECTED,
            CellCode.RED_KING,
            CellCode.RED_KING_SELECTED,
        )

    def is_black_piece(self):
        return self in (
            CellCode.BLACK_MEN,
            CellCode.BLACK_MEN_SELECTED,
            CellCode.BLACK_KING,
            CellCode.BLACK_KING_SELECTED,
        )

    def is_selected(self):
        return self in (
            CellCode.RED_MEN_SELECTED,
            CellCode.RED_KING_SELECTED,
            CellCode.BLACK_MEN_SELECTED,
            CellCode.BLACK_KING_SELECTED,
        )

    def is_king(self):
        return self in (
            CellCode.RED_KING,
            CellCode.RED_KING_SELECTED,
            CellCode.BLACK_KING,
            CellCode.BLACK_KING_SELECTED,
        )

    def selected_version(self):
        if self == CellCode.RED_MEN:
            return CellCode.RED_MEN_SELECTED

        if self == CellCode.RED_KING:
            return CellCode.RED_KING_SELECTED

        if self == CellCode.BLACK_MEN:
            return CellCode.BLACK_MEN_SELECTED

        if self == CellCode.BLACK_KING:
            return CellCode.BLACK_KING_SELECTED

        return self

    def normal_version(self):
        if self == CellCode.RED_MEN_SELECTED:
            return CellCode.RED_MEN

        if self == CellCode.RED_KING_SELECTED:
            return CellCode.RED_KING

        if self == CellCode.BLACK_MEN_SELECTED:
            return CellCode.BLACK_MEN

        if self == CellCode.BLACK_KING_SELECTED:
            return CellCode.BLACK_KING

        return self