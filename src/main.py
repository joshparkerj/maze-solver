from window import Window
from maze import Maze

cell_height = 10
cell_width = 10
maze_width = 10
maze_height = 10

win = Window(cell_width * (maze_width + 2), cell_height * (maze_height + 2))

Maze(
        cell_width,
        cell_height,
        maze_height,
        maze_width,
        cell_width,
        cell_height,
        win)

win.wait_for_close()
