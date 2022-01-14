from __future__ import absolute_import


def solver_a(depth_list):
    prev_depth = depth_list[0]
    increased = 0
    for depth in depth_list:
        if depth > prev_depth:
            increased += 1
        prev_depth = depth

    return increased


def solver_b(depth_list):
    count = 0
    increased = 0
    while count + 4 <= len(depth_list):
        prev_pair = sum(depth_list[count: count + 3])
        second_pair = sum(depth_list[count + 1: count + 4])
        if second_pair > prev_pair:
            increased += 1
        count += 1
    return increased


def generate_list(string=None):
    depth_list = []

    if string is None:
        with open('day1-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                depth_list.append(int(line))
    else:
        for line in string.split('\n'):
            depth_list.append(int(line))

    return depth_list


def main():
    depth_list = generate_list()

    print(solver_a(depth_list))
    print(solver_b(depth_list))


if __name__ == '__main__':
    main()
