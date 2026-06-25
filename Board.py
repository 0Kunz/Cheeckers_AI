from CellCode import CellCode
import pyglet as pg
from Men import Men
from pathlib import Path


class Board(pg.sprite.Sprite):

    def __init__(self, board_coordinates, game_manager):
        board_img = pg.image.load('Sprites/Board.png')
        super().__init__(board_img)

        self.board_coordinates = board_coordinates
        self.board_map = game_manager.get_board_map()
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

    def draw(self):
        super().draw()

        for row_index, row in enumerate(self.board_map):
            for col_index, cell in enumerate(row):
                try:
                    cell_code = CellCode(int(cell))
                except ValueError:
                    continue

                if cell_code in self.sprite_by_cell:
                    sprite_name = self.sprite_by_cell[cell_code]
                    self.draw_at(row_index, col_index, sprite_name)


    def draw_at(self, x, y, sprite_name):
        self.mens_sprites[sprite_name].position = (self.board_coordinates.get_pixel_position(x, y) + [0])
        self.mens_sprites[sprite_name].draw()
