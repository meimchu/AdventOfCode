import unittest
from day1sort import SolverA
from day1sort import SolverB


class TestExpenseObject(unittest.TestCase):
    def test_SolverA(self):
        testArray = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(SolverA(testArray), 514579)

    def test_SolverB(self):
        testArray = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(SolverB(testArray), 241861950)


if __name__ == '__main__':
    unittest.main(verbosity=2)
