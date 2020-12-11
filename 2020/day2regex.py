from aoc_timer import time_it
import re


class PasswordPolicy():
    def __init__(self, line):
        self.pattern = re.compile(
            r"(?P<inputA>[0-9]*)-(?P<inputB>[0-9]*)\s*(?P<letter>[a-zA-Z]):\s*(?P<password>[a-zA-Z]*)")
        self.match = self.pattern.match(line)
        self._letter = self.match.group('letter')
        self._password = self.match.group('password')

        self._inputA = int(self.match.group('inputA'))
        self._inputB = int(self.match.group('inputB'))

    @property
    def countRange(self):
        return self._countRange

    @property
    def letter(self):
        return self._letter

    @property
    def password(self):
        return self._password

    @property
    def inputA(self):
        return self._inputA

    @property
    def inputB(self):
        return self._inputB

    def validateA(self):
        count = self.password.count(self.letter)
        if count >= self.inputA and count <= self.inputB:
            return True
        return False

    def validateB(self):
        posA = self.password[self.inputA - 1]
        posB = self.password[self.inputB - 1]
        if (posA == self.letter) ^ (posB == self.letter):
            return True
        return False


@time_it
def solver_a(passwordList):
    goodPasswords = 0
    for password in passwordList:
        pwObj = PasswordPolicy(password)
        if pwObj.validateA():
            goodPasswords += 1
    return goodPasswords


@time_it
def solver_b(passwordList):
    goodPasswords = 0
    for password in passwordList:
        pwObj = PasswordPolicy(password)
        if pwObj.validateB():
            goodPasswords += 1
    return goodPasswords


def main():
    passwordList = []
    with open('day2-inputs.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line not in passwordList:
                passwordList.append(line)

    print(solver_a(passwordList))
    print(solver_b(passwordList))
    print('Solved.')


if __name__ == '__main__':
    main()
