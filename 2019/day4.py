class PasswordChecker():
    def __init__(self, start_num, end_num, *kwargs):
        self.start_num = start_num
        self.end_num = end_num
        # self.digitList = []

    def IsPassword(self, num, partTwo=False):
        smallerDigitThanPrev = False
        matchCombo = 1
        hasPair = False
        checkCombo = True
        digitList = []
        for digit in str(num):
            digitList.append(digit)

        for count, digit in enumerate(digitList):
            if count == 0:
                continue
            prevDigit = digitList[count - 1]

            if digit < prevDigit:
                smallerDigitThanPrev = True
                break

            if digit == prevDigit:
                matchCombo += 1
                checkCombo = False
                if count == (len(digitList) - 1):
                    checkCombo = True
                if not partTwo:
                    hasPair = True
            else:
                checkCombo = True

            if checkCombo and partTwo:
                if matchCombo > 1:
                    if matchCombo == 2:
                        hasPair = True
                matchCombo = 1

        if not smallerDigitThanPrev and hasPair:
            return True
        return False

    def Check(self, partTwo=False):
        goodNums = 0

        for num in range(self.start_num, self.end_num + 1):
            if self.start_num < 100000 and self.end_num > 999999:
                return 0

            if self.IsPassword(num, partTwo=partTwo):
                goodNums += 1

        return goodNums


def SolveA(start_num, end_num):
    passObj = PasswordChecker(start_num, end_num)
    return passObj.Check(partTwo=False)


def SolveB(start_num, end_num):
    passObj = PasswordChecker(start_num, end_num)
    return passObj.Check(partTwo=True)


def main():
    with open('day4-inputs.txt', 'r') as f:
        line = f.readline()
    f.close()
    start_num = int(line.split('-')[0])
    end_num = int(line.split('-')[1])
    print SolveA(start_num, end_num)
    print SolveB(start_num, end_num)
    print 'Solved.'


if __name__ == '__main__':
    main()
