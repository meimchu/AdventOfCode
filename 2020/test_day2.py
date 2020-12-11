import unittest
from day2regex import solver_a
from day2regex import solver_b


testArray = ['1-3 a: abcde',
             '1-3 b: cdefg',
             '2-9 c: ccccccccc']


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(testArray), 2)

    def test_solver_b(self):

        self.assertEqual(solver_b(testArray), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
