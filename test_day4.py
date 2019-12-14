from day4 import PasswordChecker
import unittest


class TestPasswordChecker(unittest.TestCase):
    def test_PasswordChecker_OneA(self):
        self.assertTrue(self.checker.isPassword(111111, partTwo=False))

    def test_PasswordChecker_OneB(self):
        self.assertFalse(self.checker.isPassword(223450, partTwo=False))

    def test_PasswordChecker_OneC(self):
        self.assertFalse(self.checker.isPassword(123789, partTwo=False))

    def test_PasswordChecker_TwoA(self):
        self.assertTrue(self.checker.isPassword(112233, partTwo=True))

    def test_PasswordChecker_TwoB(self):
        self.assertFalse(self.checker.isPassword(123444, partTwo=True))

    def test_PasswordChecker_TwoC(self):
        self.assertTrue(self.checker.isPassword(111122, partTwo=True))

    def setUp(self):
        self.start_num = 108457
        self.end_num = 562041
        self.checker = PasswordChecker(self.start_num, self.end_num)


if __name__ == '__main__':
    unittest.main(verbosity=2)
