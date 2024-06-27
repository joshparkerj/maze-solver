from window import Window
from line import Line
from point import Point
from cell import Cell

win = Window(800, 600)

win.draw_line(Line(Point(10, 20), Point(100, 260)), 'orange')
win.draw_line(Line(Point(20, 25), Point(200, 250)), 'brown')
win.draw_line(Line(Point(30, 10), Point(300, 240)), 'silver')
win.draw_line(Line(Point(40, 15), Point(400, 230)), 'red')
win.draw_line(Line(Point(50, 5), Point(500, 220)), 'sienna')

cells = [
 Cell(100, 100, Point(10, 10), win),
 Cell(100, 100, Point(120, 10), win),
 Cell(100, 100, Point(120, 120), win),
 Cell(100, 100, Point(230, 10), win),
 Cell(100, 100, Point(230, 120), win)
]

for cell in cells:
    cell.draw()

open_walled_cells = [
 Cell(100, 100, Point(120, 230), win),
 Cell(100, 100, Point(230, 230), win),
 Cell(100, 100, Point(230, 340), win),
 Cell(100, 100, Point(340, 230), win),
 Cell(100, 100, Point(340, 340), win)
 ]
open_walled_cells[1].open_wall('left')
open_walled_cells[2].open_wall('top')
open_walled_cells[2].open_wall('right')
open_walled_cells[3].open_wall('bottom')
open_walled_cells[3].open_wall('top')
open_walled_cells[3].open_wall('right')
open_walled_cells[4].open_wall('right')
open_walled_cells[4].open_wall('bottom')
open_walled_cells[4].open_wall('top')
open_walled_cells[4].open_wall('left')

for cell in open_walled_cells:
    cell.draw()

cells[0].draw_move(open_walled_cells[4])
cells[0].draw_move(cells[1], True)
cells[1].draw_move(cells[2], True)
cells[2].draw_move(cells[3], True)
cells[3].draw_move(cells[4], True)

win.wait_for_close()
