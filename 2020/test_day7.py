import unittest
from day7 import solver_a
from day7 import solver_b
from day7 import parse


testString = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


class TestExpenseObject(unittest.TestCase):
    def test_solver_a(self):
        self.assertEqual(solver_a(parse(testString)), 4)

    def test_solver_b(self):
        self.assertEqual(solver_b(parse(testString)), 32)


if __name__ == '__main__':
    unittest.main(verbosity=2)
