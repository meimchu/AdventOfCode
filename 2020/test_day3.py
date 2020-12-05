import unittest
from day3 import SolverA
from day3 import SolverB

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
    def test_SolverA(self):
        self.assertEqual(SolverA(testArray), 7)

    def test_SolverB(self):
        self.assertEqual(SolverB(testArray), 336)


if __name__ == '__main__':
    unittest.main(verbosity=2)
