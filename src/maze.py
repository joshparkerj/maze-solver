from cell import Cell
from point import Point
from window import Window
from time import sleep


class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win: Window = None,
                 ):
        if num_rows < 1 or num_cols < 1:
            raise Exception('maze with no cells not supported!')
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [
                [Cell(
                    self.cell_size_x,
                    self.cell_size_y,
                    Point(
                        self.x1 + i * self.cell_size_x,
                        self.y1 + j * self.cell_size_y),
                    self.win)
                 for i in range(self.num_cols)]
                for j in range(self.num_rows)]
        self._break_entrance_and_exit()
        for row in self._cells:
            for cell in row:
                cell.draw()
                self._animate()

    def _draw_cell(self):
        # this method is called for in the project description here:
        # https://www.boot.dev/lessons/d2ad2d75-29a6-43f7-a88e-e8017b686fa1
        # however, it seems that the cell already has a draw method of its own
        # so...
        pass

    def _animate(self):
        if self.win:
            self.win.redraw()
            sleep(1/12)

    def _break_entrance_and_exit(self):
        maze_entrance = self._cells[0][0]
        maze_exit = self._cells[-1][-1]
        maze_entrance.open_wall('left')
        maze_exit.open_wall('right')

