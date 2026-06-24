import pyglet as pg
from Board import Board
from GameManager import GameManager

Game = pg.window.Window(caption='Cheeckers', resizable=False)
Game.set_size(821,822)


board = Board()
game_manager = GameManager(board)

@Game.event
def on_draw():
    Game.clear()
    board.draw(game_manager.board_map)
    #board.debug_draw(game_manager.board)

@Game.event
def on_mouse_press(x, y, button, modifiers):
    game_manager.click(x, y, button, modifiers)

print("Hello World")

pg.app.run()