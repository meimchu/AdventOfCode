from __future__ import absolute_import


def solver_a(string_list, instruction_dict, step):
    while step != 0:
        count = 1
        new_current_string = string_list
        while count < len(string_list):
            current_string = string_list[count - 1: count + 1]
            # print(current_string, instruction_dict[current_string])
            new_current_string = new_current_string[:count + (count - 1)] + \
                instruction_dict[current_string] + \
                new_current_string[count + (count - 1):]
            count += 1
        print(step, new_current_string)
        string_list = new_current_string
        step -= 1

    count_dict = {}
    for x in string_list:
        if x not in count_dict:
            count_dict[x] = 0
        count_dict[x] += 1
        minimum_val = min(count_dict.values())
        maximum_val = max(count_dict.values())

    # print(min(count_dict, key=count_dict.get))
    # print(count_dict)
    return maximum_val - minimum_val


def solver_b(string_list, instruction_dict, step):
    while step != 0:
        count = 1
        new_current_string = string_list
        while count < len(string_list):
            current_string = string_list[count - 1: count + 1]
            count += 1

        step -= 1


def generate_list(string=None):
    instruction_dict = {}
    if string is None:
        with open('day14-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                if line and '->' in line:
                    line = line.replace(' ', '')
                    line = line.split('->')
                    instruction_dict[line[0]] = line[1]
                elif line:
                    string_line = line
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            if line and '->' in line:
                line = line.replace(' ', '')
                line = line.split('->')
                instruction_dict[line[0]] = line[1]
            elif line:
                string_line = line

    return string_line, instruction_dict


def main():
    string_list, instruction_dict = generate_list()

    # print(solver_a(string_list, instruction_dict, 10))
    print(solver_b(string_list, instruction_dict, 10))


if __name__ == '__main__':
    main()
