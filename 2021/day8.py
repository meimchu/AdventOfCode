from __future__ import absolute_import


def solver_a(segment_list):
    # 1 is length of of 2
    # 4 is length of of 4
    # 7 is length of of 3
    # 8 is length of of 7
    frequencies = 0
    for input_lists, output_lists in segment_list:
        for output_list in output_lists:
            if len(output_list) in [2, 3, 4, 7]:
                frequencies += 1

    return frequencies


def solver_b(segment_list):
    total_sum = 0

    for input_lists, output_lists in segment_list:
        a, b, c, d, e, f, g = None, None, None, None, None, None, None
        alphabet_dict = {}

        input_lists = sorted(input_lists, key=len)
        # print(len(input_lists), input_lists)
        input_lists_set = []
        for i in range(len(input_lists)):
            input_lists_set.append(set([s for s in input_lists[i]]))

        # Index 0 should always contain the item with length of 2
        # Index 1 should always contain the item with length of 3
        # This gets us the a value due to the difference between 7 and 1
        a = list(input_lists_set[1].difference(input_lists_set[0]))[0]
        # print('a:', a)
        alphabet_dict[a] = 'a'

        # Index 3 should always contain the item with length of 5
        # Index 4 should always contain the item with length of 5
        # Index 5 should always contain the item with length of 5
        # We can find d since the middle bar is the only value that appears between values with
        # a length of five and also 4
        find_d = input_lists_set[3].intersection(
            input_lists_set[4], input_lists_set[5])
        d = list(input_lists_set[2].intersection(find_d))[0]
        # print('d:', d)
        alphabet_dict[d] = 'd'

        # Since we found d, we can use that to find b
        find_b = list(input_lists_set[2].difference(input_lists_set[0]))
        find_b.remove(d)
        b = find_b[0]
        # print('b:', b)
        alphabet_dict[b] = 'b'

        # Index 6 should always contain the item with length of 6
        # Index 7 should always contain the item with length of 6
        # Index 8 should always contain the item with length of 6
        find_f = input_lists_set[6].intersection(
            input_lists_set[7], input_lists_set[8])
        find_f.remove(a)
        find_f.remove(b)
        f = list(find_f.intersection(input_lists_set[0]))[0]
        # print('f:', f)
        alphabet_dict[f] = 'f'

        find_c = list(input_lists_set[0].difference(set(f)))
        c = find_c[0]
        # print('c:', c)
        alphabet_dict[c] = 'c'

        find_g = list(input_lists_set[6].intersection(
            input_lists_set[7], input_lists_set[8]))
        find_g.remove(a)
        find_g.remove(b)
        find_g.remove(f)
        g = find_g[0]
        # print('g:', g)
        alphabet_dict[g] = 'g'

        find_e = list(set(['a', 'b', 'c', 'd', 'e', 'f', 'g']
                          ).difference(set([a, b, c, d, f, g])))
        e = find_e[0]
        # print('e:', e)
        alphabet_dict[e] = 'e'

        num_dict = {'cf': '1',
                    'acf': '7',
                    'bcdf': '4',
                    'acdeg': '2',
                    'acdfg': '3',
                    'abdfg': '5',
                    'abcefg': '0',
                    'abdefg': '6',
                    'abcdfg': '9',
                    'abcdefg': '8'}
        # print(output_lists)
        number_str = ''
        for output_list in output_lists:
            interpreted_value = ''
            for digit in output_list:
                interpreted_value += alphabet_dict[digit]
            number_str += num_dict[''.join(sorted(interpreted_value))]
        # print(number_str)
        total_sum += int(number_str)

    return total_sum


def generate_list(string=None):
    segment_list = []
    if string is None:
        with open('day8-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                line = line.lstrip()
                input_list = []
                output_list = []
                append_list = input_list
                for x in line.split(' '):
                    if x == '|':
                        append_list = output_list
                        continue
                    append_list.append(x)
                segment_list.append((input_list, output_list))
    else:
        for line in string.split('\n'):
            line = line.rstrip()
            line = line.lstrip()
            input_list = []
            output_list = []
            append_list = input_list
            for x in line.split(' '):
                if x == '|':
                    append_list = output_list
                    continue
                append_list.append(x)
            segment_list.append((input_list, output_list))

    return segment_list


def main():
    segment_list = generate_list()

    # print(solver_a(segment_list))
    print(solver_b(segment_list))


if __name__ == '__main__':
    main()
