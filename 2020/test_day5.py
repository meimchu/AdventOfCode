import unittest
from day5binary import SolverA


class TestExpenseObject(unittest.TestCase):
    def test_SolverA(self):
        testArray = ['FBFBBFFRLR',
                     'BFFFBBFRRR',
                     'FFFBBBFRRR',
                     'BBFFBBFRLL']
        self.assertEqual(SolverA(testArray), 820)


if __name__ == '__main__':
    unittest.main(verbosity=2)
