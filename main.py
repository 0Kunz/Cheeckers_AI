import pyglet as pg
from pyglet.window import mouse
from Board import Board
from GameManager import GameManager
from BoardCoordinates import BoardCoordinates

game = pg.window.Window(caption='Cheeckers', resizable=False)
game.set_size(821,822)

boardCoordinates = BoardCoordinates()
game_manager = GameManager(boardCoordinates)
board = Board(boardCoordinates, game_manager)


@game.event
def on_draw():
    game.clear()
    board.draw()

@game.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        game_manager.click(x, y)

print("Hello World")

pg.app.run()