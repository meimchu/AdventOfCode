import unittest
from day5binary import solver_a


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        testArray = ['FBFBBFFRLR',
                     'BFFFBBFRRR',
                     'FFFBBBFRRR',
                     'BBFFBBFRLL']
        self.assertEqual(solver_a(testArray), 820)


if __name__ == '__main__':
    unittest.main(verbosity=2)
