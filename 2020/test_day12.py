import unittest
from day12 import solver_a
from day12 import solver_b
from day12 import parse


test_string = """F10
N3
F7
R90
F11"""


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(parse(test_string)), 25)

    def test_solver_b(self):
        self.assertEqual(solver_b(parse(test_string)), 286)


if __name__ == '__main__':
    unittest.main(verbosity=2)
