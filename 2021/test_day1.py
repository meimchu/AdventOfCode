import unittest
from day1 import solver_a, solver_b, generate_list

TEST = """199
200
208
210
200
207
240
269
260
263"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test), 7)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
