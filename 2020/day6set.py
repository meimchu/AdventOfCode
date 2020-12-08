from aoc_timer import time_it


@time_it
def SolverA(group_list):
    total = 0
    answer = set()
    for group in group_list:
        for person in group:
            answer.update(set(person))
        total += len(answer)
        answer = set()

    return total


@time_it
def SolverB(group_list):
    total = 0
    total_answer = set()
    for group in group_list:
        for count, person in enumerate(group):
            answer = set(person)
            if count == 0:
                total_answer = set(person)
            else:
                total_answer = total_answer.intersection(answer)
        total += len(total_answer)
        answer = set()

    return total


def parse(test_data):
    group_list = []
    people_list = []
    line_rows = test_data.count('\n')
    for lineCount, line in enumerate(test_data.splitlines()):
        if line != '':
            people_list.append(line)
            if lineCount == line_rows:
                group_list.append(people_list)
        else:
            group_list.append(people_list)
            people_list = []

    return(group_list)


def main():
    group_list = []
    lines = ''
    with open('day6-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        group_list = parse(lines)

    print(SolverA(group_list))
    print(SolverB(group_list))


if __name__ == '__main__':
    main()
