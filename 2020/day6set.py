from aoc_timer import time_it


@time_it
def SolverA(groupList):
    total = 0
    answer = set()
    for group in groupList:
        for person in group:
            answer.update(set(person))
        total += len(answer)
        answer = set()

    return total


@time_it
def SolverB(groupList):
    total = 0
    totalAnswer = set()
    for group in groupList:
        for count, person in enumerate(group):
            answer = set(person)
            if count == 0:
                totalAnswer = set(person)
            else:
                totalAnswer = totalAnswer.intersection(answer)
        total += len(totalAnswer)
        answer = set()

    return total


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
