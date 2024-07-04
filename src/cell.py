from point import Point
from line import Line
from window import Window


class Cell:
    def __init__(self, width, height, top_left: Point, win: Window = None):
        self.width = width
        self.height = height
        self.top_left = top_left
        self.win = win
        self.wall_is_closed = {
                'left': True,
                'right': True,
                'top': True,
                'bottom': True}
        self.color = 'chartreuse'

    def draw(self):
        top = self.top_left.y
        left = self.top_left.x
        bottom = top + self.height
        right = left + self.width
        top_left = Point(left, top)
        top_right = Point(right, top)
        bottom_left = Point(left, bottom)
        bottom_right = Point(right, bottom)
        lines = []
        if self.wall_is_closed['top']:
            lines.append(Line(top_left, top_right))
        if self.wall_is_closed['right']:
            lines.append(Line(top_right, bottom_right))
        if self.wall_is_closed['bottom']:
            lines.append(Line(bottom_right, bottom_left))
        if self.wall_is_closed['left']:
            lines.append(Line(bottom_left, top_left))
        if self.win:
            for line in lines:
                self.win.draw_line(line, self.color)

    def close_wall(self, wall):
        self.wall_is_closed[wall] = True

    def open_wall(self, wall):
        self.wall_is_closed[wall] = False

    def center(self):
        return Point(
                self.top_left.x + self.width // 2,
                self.top_left.y + self.height // 2)

    def draw_move(self, to_cell, undo=False):
        start = self.center()
        end = to_cell.center()
        path = Line(start, end)
        self.win.draw_line(path, 'gray' if undo else 'red')
