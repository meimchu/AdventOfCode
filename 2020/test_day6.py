import unittest
from day6 import solver_a
from day6 import solver_b
from day6 import parse


testString = """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(parse(testString)), 11)

    def test_solver_b(self):
        self.assertEqual(solver_b(parse(testString)), 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
