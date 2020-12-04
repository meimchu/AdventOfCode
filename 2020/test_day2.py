import unittest
from day2regex import SolverA
from day2regex import SolverB


class TestExpenseObject(unittest.TestCase):
    def test_SolverA(self):
        testArray = ['1-3 a: abcde',
                     '1-3 b: cdefg',
                     '2-9 c: ccccccccc']
        self.assertEqual(SolverA(testArray), 2)

    def test_SolverB(self):
        testArray = ['1-3 a: abcde',
                     '1-3 b: cdefg',
                     '2-9 c: ccccccccc']
        self.assertEqual(SolverB(testArray), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
