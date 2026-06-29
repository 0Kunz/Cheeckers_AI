from CellCode import CellCode
import pyglet as pg
from Men import Men
from pathlib import Path

class Board(pg.sprite.Sprite):

    BOARD_IMAGE_PATH = "Sprites/Board.png"
    SPRITES_DIRECTORY = Path("./Sprites")

    SPRITE_BY_CELL = {
        CellCode.RED_MEN: "Red_men",
        CellCode.RED_MEN_SELECTED: "Red_men_Selected",
        CellCode.RED_KING: "Red_king",

        CellCode.BLACK_MEN: "Black_men",
        CellCode.BLACK_MEN_SELECTED: "Black_men_Selected",
        CellCode.BLACK_KING: "Black_king",
    }

    def __init__(self, board_coordinates, game_manager):
        board_img = pg.image.load(self.BOARD_IMAGE_PATH)
        super().__init__(board_img)

        self.board_coordinates = board_coordinates
        self.board_map = game_manager.get_board_map()
        self.mens_sprites = self.load_mens_sprites()

    def load_mens_sprites(self):
        mens_sprites = {}

        for sprite_path in self.SPRITES_DIRECTORY.iterdir():
            if not sprite_path.is_file():
                continue

            sprite_name = sprite_path.stem

            if not self.is_men_sprite(sprite_name):
                continue

            mens_sprites[sprite_name] = Men(sprite_path)

        return mens_sprites

    @staticmethod
    def is_men_sprite(sprite_name):
        sprite_name_lower = sprite_name.lower()

        return (
                "men" in sprite_name_lower
                or "king" in sprite_name_lower
        )

    def draw(self):
        super().draw()

        for row_index, row in enumerate(self.board_map):
            for column_index, cell in enumerate(row):
                cell_code = self.get_cell_code(cell)

                if cell_code is None:
                    continue

                sprite_name = self.SPRITE_BY_CELL.get(cell_code)

                if sprite_name is None:
                    continue

                self.draw_at(row_index, column_index, sprite_name)

    @staticmethod
    def get_cell_code(cell):
        try:
            return CellCode(int(cell))
        except ValueError:
            return None

    def draw_at(self, row, column, sprite_name):
        sprite = self.mens_sprites.get(sprite_name)

        if sprite is None:
            return

        pixel_position = self.board_coordinates.get_pixel_position(row, column)

        sprite.position = (*pixel_position, 0)
        sprite.draw()