from unittest import TestCase, main
from maze import Maze


class Tests(TestCase):
    def maze(self, num_cols, num_rows):
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)
        return maze

    def test_maze_create_cells(self):
        with self.assertRaises(Exception):
            self.maze(9001, 0)
        with self.assertRaises(Exception):
            self.maze(0, 250)
        with self.assertRaises(Exception):
            self.maze(0, 0)
        self.maze(12, 10)
        self.maze(2400, 1)
        self.maze(120, 1000)
        # TODO: It is quite slow to create even 120_000 cells in a maze
        # See if performance can be improved
        # self.maze(1200, 10000)

    def test_maze_break_entrance_and_exit(self):
        maze = self.maze(10, 10)
        top_left_cell = maze._cells[0][0]
        bottom_right_cell = maze._cells[-1][-1]
        self.assertFalse(top_left_cell.wall_is_closed['left'])
        self.assertFalse(bottom_right_cell.wall_is_closed['right'])

    def test_maze_cells_visited_reset(self):
        maze = self.maze(10, 10)
        self.assertTrue(all(not cell.visited for row in maze._cells for cell in row))


if __name__ == '__main__':
    main()
