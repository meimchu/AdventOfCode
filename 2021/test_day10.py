import unittest
from day10 import solver_a, solver_b, generate_list

TEST = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test = generate_list(TEST)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test), 26397)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test), 288957)


if __name__ == '__main__':
    unittest.main(verbosity=2)
