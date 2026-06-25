import numpy as np

from CellCode import CellCode
from GamesRules import GamesRules
class GameManager:

    def __init__(self, board_coordinates):
        self.board_map = np.array([ [0 , 66, 0 , 66, 0 , 66, 0 , 66],
                                         [66, 0 , 66, 0 , 66, 0 , 66, 0 ],
                                         [0 , 66, 0 , 66, 0 , 66, 0 , 66],
                                         [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 ],
                                         [0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 ],
                                         [96, 0 , 96, 0 , 96, 0 , 96, 0 ],
                                         [0 , 96, 0 , 96, 0 , 96, 0 , 96],
                                         [96, 0 , 96, 0 , 96, 0 , 96, 0 ]],dtype=np.uint8)

        self.board_coordinates = board_coordinates
        self.games_rules = GamesRules(self.board_map)
        self.game_states = { 'Has_men_selected' : False,}
        self.men_selected = []
        self.mens_states = { 'select' : 7,
                             'normal' : 6,
                             'king' : 8}
        self.players = { 'BLACK': 9,
                         'RED' : 6}
        self.player = self.players['BLACK']

    def click(self, x, y):
        tile_clicked_coordinates = self.board_coordinates.get_tile_by_pixel(x, y)
        code_tile_clicked = self.board_map[tile_clicked_coordinates[0],tile_clicked_coordinates[1]] // 10
        if self.game_states['Has_men_selected']:
            valid_moves = self.games_rules.get_valid_moves(self.men_selected)
            if tile_clicked_coordinates in valid_moves:
                pass
            else:
                self.update_board_map(self.men_selected, self.mens_states['normal'])
                self.unselect_men()

        else:
            if code_tile_clicked == self.player:
                self.update_board_map(tile_clicked_coordinates, self.mens_states['select'])
                self.select_men()
                self.men_selected = tile_clicked_coordinates

    def get_board_map(self):
        return self.board_map

    def get_element(self, lista):
        return self.board_map[lista[0]][lista[1]]

    def update_board_map(self, coordinates, action):
        player_action = int(str(self.player) + str(action))
        self.board_map[coordinates[0], coordinates[1]] = player_action

    def select_men(self):
        self.game_states["Has_men_selected"] = True

    def unselect_men(self):
        self.game_states["Has_men_selected"] = False
