import unittest
from day3 import solver_a
from day3 import solver_b

testArray = ['..##.......',
             '#...#...#..',
             '.#....#..#.',
             '..#.#...#.#',
             '.#...##..#.',
             '..#.##.....',
             '.#.#.#....#',
             '.#........#',
             '#.##...#...',
             '#...##....#',
             '.#..#...#.#']


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(testArray), 7)

    def test_solver_b(self):
        self.assertEqual(solver_b(testArray), 336)


if __name__ == '__main__':
    unittest.main(verbosity=2)
