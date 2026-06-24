import pyglet as pg

class Men(pg.sprite.Sprite):

    def __init__(self, name_sprite):
        board_img = pg.image.load(name_sprite)
        super().__init__(board_img)
        self.isKing = False
