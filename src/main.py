from window import Window
from maze import Maze

cell_height = 33
cell_width = 33
maze_width = 53
maze_height = 31

win = Window(cell_width * (maze_width + 2), cell_height * (maze_height + 2))

m = Maze(
        cell_width,
        cell_height,
        maze_height,
        maze_width,
        cell_width,
        cell_height,
        win=win,
        animate_speed=1/72)

m.solve()

win.wait_for_close()
