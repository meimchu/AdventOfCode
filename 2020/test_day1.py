import unittest
from day1sort import solver_a
from day1sort import solver_b


testArray = [1721, 979, 366, 299, 675, 1456]


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(testArray), 514579)

    def test_solver_b(self):
        self.assertEqual(solver_b(testArray), 241861950)


if __name__ == '__main__':
    unittest.main(verbosity=2)
