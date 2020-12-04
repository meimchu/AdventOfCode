import unittest
from day4 import SolverA
# from day4 import SolverB
from day4 import Passport


class TestExpenseObject(unittest.TestCase):
    def test_SolverA(self):
        testArray = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
                     'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
                     'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm',
                     'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in']
        self.assertEqual(SolverA(testArray), 2)

    def test_ValidateByr(self):
        testDict = {'byr': '2002'}
        passportObj = Passport(testDict)
        self.assertTrue(passportObj.validateByr())

        testDict = {'byr': '2003'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validateByr())

    def test_ValidateHgt(self):
        testDict = {'hgt': '60in'}
        passportObj = Passport(testDict)
        self.assertTrue(passportObj.validateHgt())

        testDict = {'hgt': '190cm'}
        passportObj = Passport(testDict)
        self.assertTrue(passportObj.validateHgt())

        testDict = {'hgt': '190in'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validateHgt())

        testDict = {'hgt': '190'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validateHgt())
    
    def test_ValidateHcl(self):
        testDict = {'hcl': '#123abc'}
        passportObj = Passport(testDict)
        self.assertTrue(passportObj.validateHcl())

        testDict = {'hcl': '#123abz'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validateHcl())

        testDict = {'hcl': '123abc'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validateHcl())

    def test_ValidateEcl(self):
        testDict = {'ecl': 'brn'}
        passportObj = Passport(testDict)
        self.assertTrue(passportObj.validateEcl())

        testDict = {'ecl': 'wat'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validateEcl())
    
    def test_ValidatePid(self):
        testDict = {'pid': '000000001'}
        passportObj = Passport(testDict)
        self.assertTrue(passportObj.validatePid())

        testDict = {'pid': '0123456789'}
        passportObj = Passport(testDict)
        self.assertFalse(passportObj.validatePid())

if __name__ == '__main__':
    unittest.main(verbosity=2)
