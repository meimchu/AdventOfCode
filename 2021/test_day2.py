import unittest
from day2 import solver_a, solver_b, generate_list

TEST = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test), 150)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test), 900)


if __name__ == '__main__':
    unittest.main(verbosity=2)
