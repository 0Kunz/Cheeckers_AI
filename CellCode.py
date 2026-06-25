from enum import IntEnum

class CellCode(IntEnum):
    NOT_PLAYABLE = 0
    EMPTY_PLAYABLE = 1

    RED_MEN = 66
    RED_MEN_SELECTED = 67
    RED_KING = 68

    BLACK_MEN = 96
    BLACK_MEN_SELECTED = 97
    BLACK_KING = 98