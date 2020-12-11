import unittest
from day10 import solver_a
from day10 import solver_b
from day10 import parse


test_string_1 = """16
10
15
5
1
11
7
19
6
12
4"""

test_string_2 ="""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

class TestExpenseObject(unittest.TestCase):
    def test_solver_a_1(self):
        self.assertEqual(solver_a(parse(test_string_1)), 35)
    
    def test_solver_a_2(self):
        self.assertEqual(solver_a(parse(test_string_2)), 220)

    def test_solver_b_1(self):
        self.assertEqual(solver_b(parse(test_string_1)), 8)

    def test_solver_b_2(self):
        self.assertEqual(solver_b(parse(test_string_2)), 19208)


if __name__ == '__main__':
    unittest.main(verbosity=2)
