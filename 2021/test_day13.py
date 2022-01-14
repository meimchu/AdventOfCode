import unittest
from day13 import solver_a, solver_b, generate_list

TEST = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test, self.fold_instruction_list = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test, self.fold_instruction_list, 1), 17)

    # def test_solver_b(self):
    #     self.assertEqual(solver_b(self.test, self.fold_instruction_list), 'O')


if __name__ == '__main__':
    unittest.main(verbosity=2)
