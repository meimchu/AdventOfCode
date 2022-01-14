import unittest
from day9 import solver_a, solver_b, generate_list

TEST = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test), 15)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test), 1134)


if __name__ == '__main__':
    unittest.main(verbosity=2)
