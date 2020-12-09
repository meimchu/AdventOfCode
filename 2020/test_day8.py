import unittest
from day8class import SolverA
from day8class import SolverB
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
    def test_SolverA(self):
        self.assertEqual(SolverA(parse(testString)), 5)

    def test_SolverB(self):
        self.assertEqual(SolverB(parse(testString)), 8)


if __name__ == '__main__':
    unittest.main(verbosity=2)
