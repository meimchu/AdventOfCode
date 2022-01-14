from __future__ import absolute_import


def solver_a(bracket_list):
    bracket_dict = {'>': '<',
                    ')': '(',
                    ']': '[',
                    '}': '{'}
    corrupt_list = []

    for row in bracket_list:
        right = len(row) - 1
        while right >= 0:
            # print(right)
            right_bracket = row[right]
            if right_bracket in bracket_dict:
                left = right - 1
                left_bracket = row[left]
                if left_bracket == bracket_dict[right_bracket]:
                    row.pop(right)
                    row.pop(left)
                    # print('remove %s %s' % (left_bracket, right_bracket))
                    right = len(row) - 1
                else:
                    right -= 1
            else:
                right -= 1

        corrupt_dict = {'>': 25137,
                        ')': 3,
                        ']': 57,
                        '}': 1197}
        for r in row:
            if r in bracket_dict:
                corrupt_list.append(corrupt_dict[r])
                break

    return sum(corrupt_list)


def solver_b(bracket_list):
    bracket_dict = {'>': '<',
                    ')': '(',
                    ']': '[',
                    '}': '{'}
    incomplete_list = []

    for row in bracket_list:
        right = len(row) - 1
        while right >= 0:
            # print(right)
            right_bracket = row[right]
            if right_bracket in bracket_dict:
                left = right - 1
                left_bracket = row[left]
                if left_bracket == bracket_dict[right_bracket]:
                    row.pop(right)
                    row.pop(left)
                    # print('remove %s %s' % (left_bracket, right_bracket))
                    right = len(row) - 1
                else:
                    right -= 1
            else:
                right -= 1

        incomplete_dict = {'<': 4,
                           '(': 1,
                           '[': 2,
                           '{': 3}
        incomplete_sum = 0
        right = len(row) - 1
        while right >= 0:
            incomplete_sum *= 5
            r = row[right]
            if r in incomplete_dict:
                incomplete_sum += incomplete_dict[r]
            else:
                incomplete_sum = 0
                break
            right -= 1
        if incomplete_sum != 0:
            incomplete_list.append(incomplete_sum)
    mid_index = len(incomplete_list) // 2
    return sorted(incomplete_list)[mid_index]


def generate_list(string=None):
    row_list = []
    if string is None:
        with open('day10-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                col_list = []
                for x in line:
                    col_list.append(x)
                row_list.append(col_list)
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            col_list = []
            for x in line:
                col_list.append(x)
            row_list.append(col_list)

    return row_list


def main():
    bracket_list = generate_list()

    print(solver_a(bracket_list))
    print(solver_b(bracket_list))


if __name__ == '__main__':
    main()
