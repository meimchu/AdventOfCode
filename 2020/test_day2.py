import unittest
from day2regex import SolverA
from day2regex import SolverB


testArray = ['1-3 a: abcde',
             '1-3 b: cdefg',
             '2-9 c: ccccccccc']


class TestExpenseObject(unittest.TestCase):
    def test_SolverA(self):
        self.assertEqual(SolverA(testArray), 2)

    def test_SolverB(self):

        self.assertEqual(SolverB(testArray), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
