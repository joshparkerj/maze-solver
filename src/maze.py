from cell import Cell
from point import Point
from window import Window
from time import sleep
from random import seed, choice
from sys import setrecursionlimit


class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 animate_speed: float = 1/24,
                 win: Window = None,
                 random_seed=None,
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
        seed(random_seed)
        self.animate_speed = animate_speed
        self._create_cells()
        self._reset_cells_visited()

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
        setrecursionlimit(self.num_rows * self.num_cols * 2)
        self._break_walls_r(0, 0)
        for i, row in enumerate(self._cells):
            for j, cell in enumerate(row):
                if not cell.visited:
                    self._break_walls_r(i, j, True)
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
            sleep(self.animate_speed)

    def _break_entrance_and_exit(self):
        maze_entrance = self._cells[0][0]
        maze_exit = self._cells[-1][-1]
        maze_entrance.open_wall('left')
        maze_exit.open_wall('right')

    def _visit(self, current_cell, to_visit_choices):
        to_visit = choice(to_visit_choices)
        cell = to_visit[0]
        if to_visit[1] == 'left':
            current_cell.open_wall('left')
            cell.open_wall('right')
        if to_visit[1] == 'right':
            current_cell.open_wall('right')
            cell.open_wall('left')
        if to_visit[1] == 'up':
            current_cell.open_wall('top')
            cell.open_wall('bottom')
        if to_visit[1] == 'down':
            current_cell.open_wall('bottom')
            cell.open_wall('top')
        return to_visit

    def _break_walls_r(self, i, j, needs_visited=False):
        current_cell = self._cells[i][j]
        if current_cell.visited:
            raise Exception('revisited cell after visiting already!')
        current_cell.visited = True
        new_neighbors = []
        visited_neighbors = []
        if i > 0:
            neighbor = (self._cells[i - 1][j], 'up', i - 1, j)
            if neighbor[0].visited:
                visited_neighbors.append(neighbor)
            else:
                new_neighbors.append(neighbor)
        if j > 0:
            neighbor = (self._cells[i][j - 1], 'left', i, j - 1)
            if neighbor[0].visited:
                visited_neighbors.append(neighbor)
            else:
                new_neighbors.append(neighbor)
        if i < len(self._cells) - 1:
            neighbor = (self._cells[i + 1][j], 'down', i + 1, j)
            if neighbor[0].visited:
                visited_neighbors.append(neighbor)
            else:
                new_neighbors.append(neighbor)
        if j < len(self._cells[i]) - 1:
            neighbor = (self._cells[i][j + 1], 'right', i, j + 1)
            if neighbor[0].visited:
                visited_neighbors.append(neighbor)
            else:
                new_neighbors.append(neighbor)
        if needs_visited:
            if len(visited_neighbors) == 0:
                raise Exception('No visited neighbor!')
            self._visit(current_cell, visited_neighbors)
        if len(new_neighbors) == 0:
            return
        to_visit = self._visit(current_cell, new_neighbors)
        self._break_walls_r(to_visit[2], to_visit[3])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
