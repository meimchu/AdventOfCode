import unittest
from day14 import solver_a, solver_b, generate_list

TEST = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test, self.fold_instruction_list = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test, self.fold_instruction_list, 10), 1588)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test, self.fold_instruction_list, 20), 2188189693529)


if __name__ == '__main__':
    unittest.main(verbosity=2)
