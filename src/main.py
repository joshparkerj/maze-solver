from window import Window
from maze import Maze

cell_height = 20
cell_width = 20
maze_width = 12
maze_height = 9

win = Window(cell_width * (maze_width + 2), cell_height * (maze_height + 2))

Maze(
        cell_width,
        cell_height,
        maze_height,
        maze_width,
        cell_width,
        cell_height,
        win=win)

win.wait_for_close()
