import unittest
from day5 import solver_a, solver_b, generate_list

TEST = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test), 5)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test), 12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
