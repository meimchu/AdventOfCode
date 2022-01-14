import unittest
from day12 import solver_a, solver_b, generate_list

TEST_ONE = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST_TWO = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

TEST_THREE = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


class TestSolver(unittest.TestCase):
    def setUp(self):
        self.test_one = generate_list(TEST_ONE)
        self.test_two = generate_list(TEST_TWO)
        self.test_three = generate_list(TEST_THREE)

    def test_solver_a(self):
        self.assertEqual(solver_a(self.test_one), 10)
        self.assertEqual(solver_a(self.test_two), 19)
        self.assertEqual(solver_a(self.test_three), 226)

    def test_solver_b(self):
        self.assertEqual(solver_b(self.test_one), 36)
        self.assertEqual(solver_b(self.test_two), 103)
        self.assertEqual(solver_b(self.test_three), 3509)


if __name__ == '__main__':
    unittest.main(verbosity=2)
