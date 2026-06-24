from CellCode import CellCode
import pyglet as pg
from Men import Men
from pathlib import Path


class Board(pg.sprite.Sprite):

    def __init__(self):
        board_img = pg.image.load('Sprites/Board.png')
        super().__init__(board_img)

        self.mens_sprites = {}

        directory = Path("./Sprites")
        for sprite in directory.iterdir():
            if sprite.is_file() and ("king" in sprite.name or "men" in sprite.name):
                ns_without_extention = str(sprite.name.rsplit(".",1)[0])
                self.mens_sprites[ns_without_extention] = Men(sprite)

        self.sprite_by_cell = {
            CellCode.RED_MEN: "Red_men",
            CellCode.RED_MEN_SELECTED: "Red_men_Selected",
            CellCode.RED_KING: "Red_king",

            CellCode.BLACK_MEN: "Black_men",
            CellCode.BLACK_MEN_SELECTED: "Black_men_Selected",
            CellCode.BLACK_KING: "Black_king",
        }

        self.map_coordinates = [[], [], [], [], [], [], [], []]
        x = 22
        y = 702
        distance_tile = 97
        for row in range(0, 8):
            for line in range(0, 8):
                self.map_coordinates[row].append([x, y])
                x = x + distance_tile
            y = y - distance_tile
            x = 22

    def draw(self, board_map):
        super().draw()

        for row_index, row in enumerate(board_map):
            for col_index, cell in enumerate(row):
                cell_code =  int(cell)
                if cell_code in self.sprite_by_cell:
                    sprite_name = self.sprite_by_cell[cell_code]
                    self.draw_at(row_index, col_index, sprite_name)


    def draw_at(self, x, y, sprite_name):
        self.mens_sprites[sprite_name].position = (self.map_coordinates[x][y] + [0])
        self.mens_sprites[sprite_name].draw()

    def debug_draw(self, board_map):
        self.mens_sprites['Red_men'].position = (119, 702, 0)
        self.mens_sprites['Red_men'].draw()
