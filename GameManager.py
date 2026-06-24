import numpy as np

class GameManager:

    def __init__(self, board):
        self.board = board
        self.board_map = np.array([ [0 , 66, 0 , 66, 0 , 66, 0 , 66],
                                         [66, 0 , 66, 0 , 66, 0 , 66, 0 ],
                                         [0 , 66, 0 , 66, 0 , 66, 0 , 66],
                                         [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 ],
                                         [0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 ],
                                         [97, 0 , 97, 0 , 97, 0 , 97, 0 ],
                                         [0 , 97, 0 , 97, 0 , 97, 0 , 97],
                                         [97, 0 , 97, 0 , 97, 0 , 97, 0 ]],dtype=np.uint8)

        #board.update_board(self.board_map)

    def click(self, x, y, button, modifiers):
        self.board.update_board(self.board_map)
        pass