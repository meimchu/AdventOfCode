import unittest
from day9 import PreambleCode
from day9 import parse


testString = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        preambleObj = PreambleCode(parse(testString), 5)
        while True:
            if preambleObj.continue_transmit():
                preambleObj.step()
            else:
                break
        self.assertEqual(preambleObj.no_match, 127)

    def test_solver_b(self):
        preambleObj = PreambleCode(parse(testString), 5)
        preambleObj.target = 127
        while True:
            if preambleObj.continue_transmit():
                preambleObj.step()
            else:
                break
        weakness_list = sorted(preambleObj.total_list)
        self.assertEqual((weakness_list[0] + weakness_list[-1]), 62)


if __name__ == '__main__':
    unittest.main(verbosity=2)
