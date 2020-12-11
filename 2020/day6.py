from aoc_timer import time_it


class GroupAnswers():
    def __init__(self, group_list):
        self._group_list = group_list
        self._total = 0
        self._total_b = 0
        self._group_answer = set()
        self._group_answer_b = set()

        self.group_answers()

    @property
    def group_list(self):
        return self._group_list

    def group_answers(self):
        for count, person in enumerate(self.group_list):
            answer = set(person)
            self._group_answer.update(answer)
            if count == 0:
                self._group_answer_b = answer
            self._group_answer_b = self._group_answer_b.intersection(answer)
        self._total += len(self._group_answer)
        self._total_b += len(self._group_answer_b)

        return self._group_answer

    def group_answers_count(self):
        return self._total

    def full_group_answers(self):
        return self._group_answer_b

    def frull_group_answers_count(self):
        return self._total_b


@time_it
def solver_a(group_dict_list):
    total_answers = 0
    for group_dict in group_dict_list:
        groupObj = GroupAnswers(group_dict)
        total_answers += groupObj.group_answers_count()

    return total_answers


@time_it
def solver_b(group_dict_list):
    total_answers = 0
    for group_dict in group_dict_list:
        groupObj = GroupAnswers(group_dict)
        total_answers += groupObj.frull_group_answers_count()

    return total_answers


def parse(textData):
    group_list = []
    people_list = []
    lineRows = textData.count('\n')
    for lineCount, line in enumerate(textData.splitlines()):
        if line != '':
            people_list.append(line)
            if lineCount == lineRows:
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

    print(solver_a(group_list))
    print(solver_b(group_list))


if __name__ == '__main__':
    main()
