from aoc_timer import time_it
import re


class Passport():
    MUST_HAVE = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    def __init__(self, passportDict, additionalCheck=False):
        self._passportDict = passportDict
        self.additionalCheck = additionalCheck

    def validate(self):
        if all(elem in self._passportDict.keys() for elem in self.MUST_HAVE):
            if self.additionalCheck:
                if not self.validateByr():
                    return False
                if not self.validateIyr():
                    return False
                if not self.validateEyr():
                    return False
                if not self.validateHgt():
                    return False
                if not self.validateHcl():
                    return False
                if not self.validateEcl():
                    return False
                if not self.validatePid():
                    return False
                return True
            return True
        return False

    def validateByr(self):
        byr = self._passportDict.get('byr')
        if len(byr) != 4:
            return False
        if int(byr) >= 1920 and int(byr) <= 2002:
            return True
        return False

    def validateIyr(self):
        iyr = self._passportDict.get('iyr')
        if len(iyr) != 4:
            return False
        if int(iyr) >= 2010 and int(iyr) <= 2020:
            return True
        return False

    def validateEyr(self):
        eyr = self._passportDict.get('eyr')
        if len(eyr) != 4:
            return False
        if int(eyr) >= 2020 and int(eyr) <= 2030:
            return True
        return False

    def validateHgt(self):
        hgt = self._passportDict.get('hgt')
        pattern = re.compile(r"(?P<num>[0-9]*)(?P<dem>\D*)")
        match = pattern.match(hgt)
        num = int(match.group('num')) or 0
        dem = match.group('dem') or None
        if dem == 'cm' and (150 <= num <= 193):
            return True
        elif dem == 'in' and (59 <= num <= 76):
            return True
        else:
            return False

    def validateHcl(self):
        hcl = self._passportDict.get('hcl')
        pattern = re.compile(r"#[0-9a-f]{6}")
        match = pattern.match(hcl)
        if match:
            return True
        return False

    def validateEcl(self):
        ecl = self._passportDict.get('ecl')
        if ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return True
        return False

    def validatePid(self):
        pid = self._passportDict.get('pid')
        pattern = re.compile(r"^([0-9]{9})$")
        match = pattern.match(pid)
        if match:
            return True
        return False


@time_it
def SolverA(passportList):
    goodPassports = 0
    for passport in passportList:
        passportDict = {}
        for items in passport.split(' '):
            key, value = items.split(':')
            passportDict[key] = value
        passportObj = Passport(passportDict)
        if passportObj.validate():
            goodPassports += 1

    return goodPassports


@time_it
def SolverB(passportList):
    goodPassports = 0
    for passport in passportList:
        passportDict = {}
        for items in passport.split(' '):
            key, value = items.split(':')
            passportDict[key] = value
        passportObj = Passport(passportDict, True)
        if passportObj.validate():
            goodPassports += 1

    return goodPassports


def main():
    passportList = ['']
    with open('day4-inputs.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line != '':
                oldLine = passportList.pop(-1)
                if oldLine != '':
                    oldLine += ' '
                line = oldLine + line
                passportList.append(line)
            else:
                passportList.append('')

    print(SolverA(passportList))
    print(SolverB(passportList))
    print('Solved.')


if __name__ == '__main__':
    main()
