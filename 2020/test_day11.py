import unittest
from day11 import solver_a
from day11 import solver_b
from day11 import parse


test_string = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


class TestExpenseObject(unittest.TestCase):
    def test_solver_a_1(self):
        self.assertEqual(solver_a(parse(test_string)), 37)

    def test_solver_b_1(self):
        self.assertEqual(solver_b(parse(test_string)), 26)


if __name__ == '__main__':
    unittest.main(verbosity=2)
