from unittest import TestCase, main
from maze import Maze


class Tests(TestCase):
    def maze(self, num_cols, num_rows):
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_rows)
        self.assertEqual(len(maze._cells[0]), num_cols)

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
        # self.maze(1200, 10000)


if __name__ == '__main__':
    main()
