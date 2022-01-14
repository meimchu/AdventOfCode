from __future__ import absolute_import


def solver_a(fold_list, fold_instruction_list, limit=None):
    get_grid(fold_list)
    largest_x = 0
    largest_y = 0

    for axis, fold_value in fold_instruction_list:
        print('fold along %s=%s' % (axis, fold_value))
        new_fold_list = []
        for x, y in fold_list:
            if axis == 'y':
                largest_y = fold_value
                if y > fold_value:
                    new_y = y - ((y - fold_value) * 2)
                    new_fold_list.append((x, new_y))
                else:
                    new_fold_list.append((x, y))
            elif axis == 'x':
                largest_x = fold_value
                if x > fold_value:
                    new_x = x - ((x - fold_value) * 2)
                    new_fold_list.append((new_x, y))
                else:
                    new_fold_list.append((x, y))
        fold_list = new_fold_list
        if axis == 'y':
            dot_count = get_grid(fold_list, largest_x=largest_x, largest_y=largest_y)
        else:
            dot_count = get_grid(fold_list, largest_x=largest_x, largest_y=largest_y)

        if limit is not None:
            limit -= 1
        if limit == 0:
            break

    return dot_count


def solver_b(fold_list, fold_instruction_list):
    get_grid(fold_list)
    largest_x = 0
    largest_y = 0

    fold_instruction_list_len = len(fold_instruction_list)
    count = 0
    for axis, fold_value in fold_instruction_list:
        print('fold along %s=%s' % (axis, fold_value))
        new_fold_list = []
        for x, y in fold_list:
            if axis == 'y':
                largest_y = fold_value
                if y > fold_value:
                    new_y = y - ((y - fold_value) * 2)
                    new_fold_list.append((x, new_y))
                else:
                    new_fold_list.append((x, y))
            elif axis == 'x':
                largest_x = fold_value
                if x > fold_value:
                    new_x = x - ((x - fold_value) * 2)
                    new_fold_list.append((new_x, y))
                else:
                    new_fold_list.append((x, y))
        fold_list = new_fold_list
        count += 1
        if axis == 'y':
            get_grid(fold_list, largest_x, largest_y,
                       count == fold_instruction_list_len)
        else:
            get_grid(fold_list, largest_x, largest_y,
                       count == fold_instruction_list_len)


def get_grid(fold_list, largest_x=0, largest_y=0, print_grid=False):
    if not fold_list:
        return

    largest_x = largest_x - 1 or 0
    largest_y = largest_y - 1 or 0
    dot_count = 0
    for x, y in fold_list:
        largest_x = max(largest_x, x)
        largest_y = max(largest_y, y)

    for row in range(largest_y + 1):
        row_list = []
        for col in range(largest_x + 1):
            if (col, row) in fold_list:
                dot_count += 1
                row_list.append('#')
            else:
                row_list.append('.')
        if print_grid:
            print(row_list)
    return dot_count


def generate_list(string=None):
    row_list = []
    fold_instruction_list = []
    if string is None:
        with open('day13-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                if line and 'fold along' not in line:
                    line = line.split(',')
                    row_list.append((int(line[0]), int(line[1])))
                elif line:
                    line = line.replace(' ', '')
                    line = line.split('=')
                    fold_axis = line[0][-1:]
                    value = int(line[-1])
                    fold_instruction_list.append((fold_axis, value))
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            if line and 'fold along' not in line:
                line = line.split(',')
                row_list.append((int(line[0]), int(line[1])))
            elif line:
                line = line.replace(' ', '')
                line = line.split('=')
                fold_axis = line[0][-1:]
                value = int(line[-1])
                fold_instruction_list.append((fold_axis, value))

    return row_list, fold_instruction_list


def main():
    fold_list, fold_instruction_list = generate_list()

    print(solver_a(fold_list, fold_instruction_list, 1))
    print(solver_b(fold_list, fold_instruction_list))


if __name__ == '__main__':
    main()
