from __future__ import absolute_import

import sys


def solver_a(crab_list):
    smallest_diff = None
    crab_dict = {}
    sorted_crab_list = sorted(crab_list)
    for ref_crab in range(1, sorted_crab_list[-1] + 1):
        diff = 0
        if ref_crab in crab_dict:
            diff = crab_dict[ref_crab]
        else:
            for crab in crab_list:
                diff += abs(crab - ref_crab)
            crab_dict[ref_crab] = diff

        if smallest_diff:
            smallest_diff = min(smallest_diff, diff)
        else:
            smallest_diff = diff

    return smallest_diff


MEMO = {}


def crab_sum(val):
    global MEMO

    if val in MEMO:
        return MEMO[val]
    if val == 1:
        return 1
    if val < 1:
        return 0
    MEMO[val] = crab_sum(val - 1) + val
    return MEMO[val]


def solver_b(crab_list):
    sys.setrecursionlimit(2000)

    smallest_diff = None
    crab_dict = {}
    sorted_crab_list = sorted(crab_list)
    for ref_crab in range(1, sorted_crab_list[-1] + 1):
        total_diff = 0
        if ref_crab in crab_dict:
            total_diff = crab_dict[ref_crab]
        else:
            for crab in crab_list:
                diff = abs(crab - ref_crab)
                diff = crab_sum(diff)
                total_diff += diff
            crab_dict[ref_crab] = total_diff

        if smallest_diff:
            smallest_diff = min(smallest_diff, total_diff)
        else:
            smallest_diff = total_diff

    sys.setrecursionlimit(1000)
    return smallest_diff


def generate_list(string=None):
    crab_list = []
    if string is None:
        with open('day7-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                for x in line.split(','):
                    crab_list.append(int(x))
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            for x in line.split(','):
                crab_list.append(int(x))

    return crab_list


def main():
    crab_list = generate_list()

    print(solver_a(crab_list))
    print(solver_b(crab_list))


if __name__ == '__main__':
    main()
