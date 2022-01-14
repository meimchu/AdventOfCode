import unittest
from day3 import solver_a, solver_b, generate_list

TEST = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test), 198)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test), 230)


if __name__ == '__main__':
    unittest.main(verbosity=2)
