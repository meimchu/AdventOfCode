from aoc_timer import time_it


class ExpenseObject():
    def __init__(self, expense_list, target):
        self._expense_list = sorted(expense_list)
        self._reversed_expense_list = sorted(expense_list, reverse=True)
        self._target = target

        self._input_loc_a = 0
        self._input_loc_b = 0

    @property
    def target(self):
        return self._target

    @property
    def expense_list(self):
        return self._expense_list

    @property
    def reversed_expense_list(self):
        return self._reversed_expense_list

    @property
    def expense_list_length(self):
        return len(self._expense_list)

    @property
    def input_loc_a(self):
        return self._input_loc_a

    @input_loc_a.setter
    def input_loc_a(self, a):
        self._input_loc_a = a

    @property
    def input_loc_b(self):
        return self._input_loc_b

    @input_loc_b.setter
    def input_loc_b(self, b):
        self._input_loc_b = b


@time_it
def solver_a(expense_list):
    exp = ExpenseObject(expense_list, 2020)
    exp_length = exp.expense_list_length
    exp_list = exp.expense_list
    reversed_exp_list = exp.reversed_expense_list
    exp_target = exp.target

    input_loc_a = 0
    input_loc_b = 0
    while input_loc_a < exp_length:
        input_a = reversed_exp_list[input_loc_a]
        if input_a >= exp_target:
            continue

        while input_loc_b < exp_length:
            input_b = exp_list[input_loc_b]
            if (input_a + input_b) > exp_target:
                break
            elif (input_a + input_b) == exp_target:
                return (input_a * input_b)
            input_loc_b += 1

        input_loc_a += 1
        input_loc_b = 0
    return None


@time_it
def solver_b(expense_list):
    exp = ExpenseObject(expense_list, 2020)
    exp_length = exp.expense_list_length
    exp_list = exp.expense_list
    reversed_exp_list = exp.reversed_expense_list
    exp_target = exp.target

    input_loc_a = 0
    input_loc_b = 0
    input_loc_c = 0
    while input_loc_a < exp_length:
        input_a = reversed_exp_list[input_loc_a]
        msg = str(input_a)
        if input_a >= exp_target:
            continue

        while input_loc_b < exp_length:
            input_b = exp_list[input_loc_b]
            msg = msg + ' ' + str(input_b)
            if (input_a + input_b) > exp_target:
                break

            while input_loc_c < exp_length:
                input_c = exp_list[input_loc_c]
                msg = msg + ' ' + str(input_c)
                if (input_a + input_b + input_c) > exp_target:
                    break
                elif (input_a + input_b + input_c) == exp_target:
                    return (input_a * input_b * input_c)

                input_loc_c += 1

            input_loc_b += 1
            input_loc_c = 0

        input_loc_a += 1
        input_loc_b = 0
    return None


def main():
    expense_list = []
    with open('day1-inputs.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            if line not in expense_list:
                expense_list.append(int(line))

    print(solver_a(expense_list))
    print(solver_b(expense_list))
    print('Solved.')


if __name__ == '__main__':
    main()
