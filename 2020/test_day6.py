import unittest
from day6 import SolverA
from day6 import SolverB
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
    def test_SolverA(self):
        self.assertEqual(SolverA(parse(testString)), 11)

    def test_SolverB(self):
        self.assertEqual(SolverB(parse(testString)), 6)


if __name__ == '__main__':
    unittest.main(verbosity=2)
