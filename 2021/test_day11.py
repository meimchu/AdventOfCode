import unittest
from day11 import solver_a, solver_b, generate_list

TEST_ONE = """11111
19991
19191
19991
11111"""

TEST_TWO = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test_one = generate_list(TEST_ONE)
        self.test_two = generate_list(TEST_TWO)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test_one, 2), 9)
        # self.assertEqual(solver_a(self.test_two, 10), 204)
        self.assertEqual(solver_a(self.test_two, 100), 1656)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test_two), 195)


if __name__ == '__main__':
    unittest.main(verbosity=2)
