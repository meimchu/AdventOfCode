import unittest
from day3 import SolverA
from day3 import SolverB


class TestExpenseObject(unittest.TestCase):
    def test_SolverA(self):
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
        self.assertEqual(SolverA(testArray), 7)

    def test_SolverB(self):
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
        self.assertEqual(SolverB(testArray), 336)


if __name__ == '__main__':
    unittest.main(verbosity=2)
