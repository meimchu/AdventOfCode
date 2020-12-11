import unittest
from day8class import solver_a
from day8class import solver_b
from day8class import parse


testString = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(parse(testString)), 5)

    def test_solver_b(self):
        self.assertEqual(solver_b(parse(testString)), 8)


if __name__ == '__main__':
    unittest.main(verbosity=2)
