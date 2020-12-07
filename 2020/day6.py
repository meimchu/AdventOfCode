from aoc_timer import time_it


class GroupAnswers():
    def __init__(self, groupList):
        self._groupList = groupList
        self._total = 0
        self._totalB = 0
        self._groupAnswer = set()
        self._groupAnswerB = set()

        self.groupAnswers()

    @property
    def groupList(self):
        return self._groupList

    def groupAnswers(self):
        for count, person in enumerate(self.groupList):
            answer = set(person)
            self._groupAnswer.update(answer)
            if count == 0:
                self._groupAnswerB = answer
            self._groupAnswerB = self._groupAnswerB.intersection(answer)
        self._total += len(self._groupAnswer)
        self._totalB += len(self._groupAnswerB)

        return self._groupAnswer

    def groupAnswersCount(self):
        return self._total

    def fullGroupAnswers(self):
        return self._groupAnswerB

    def fullGroupAnswersCount(self):
        return self._totalB


@time_it
def SolverA(groupDictList):
    totalAnswers = 0
    for groupDict in groupDictList:
        groupObj = GroupAnswers(groupDict)
        totalAnswers += groupObj.groupAnswersCount()

    return totalAnswers


@time_it
def SolverB(groupDictList):
    totalAnswers = 0
    for groupDict in groupDictList:
        groupObj = GroupAnswers(groupDict)
        totalAnswers += groupObj.fullGroupAnswersCount()

    return totalAnswers


def parse(textData):
    groupList = []
    peopleList = []
    lineRows = textData.count('\n')
    for lineCount, line in enumerate(textData.splitlines()):
        if line != '':
            peopleList.append(line)
            if lineCount == lineRows:
                groupList.append(peopleList)
        else:
            groupList.append(peopleList)
            peopleList = []

    return(groupList)


def main():
    groupList = []
    lines = ''
    with open('day6-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        groupList = parse(lines)

    print(SolverA(groupList))
    print(SolverB(groupList))


if __name__ == '__main__':
    main()
