import re


def solver_a(bit_list):
    total_mask = None
    total_sum_dict = {}
    for line in bit_list:
        divider = re.split(r"\s=\s", line)
        action = divider[0]
        value = divider[-1]
        if action == 'mask':
            total_mask = value
            # print(total_mask)
        else:
            # print action
            mem = re.findall(r"\d+", action)[0]
            binary_value = bin(int(value)).replace('0b', '')
            length_diff = len(total_mask) - len(binary_value)
            binary_value = '0' * length_diff + binary_value
            new_binary = []
            # print(binary_value)
            for c, b in enumerate(reversed(binary_value)):
                mask = total_mask[-(c+1)]
                if mask == 'X':
                    new_binary.insert(0, b)
                else:
                    new_binary.insert(0, mask)
            new_binary = ''.join(new_binary)
            total_sum_dict[mem] = int(new_binary, 2)
            # print(int(new_binary, 2))

    total_sum = 0
    for v in total_sum_dict.values():
        total_sum += v
    return total_sum


def solver_b(bit_list):
    total_mask = None
    total_sum_dict = {}
    for line in bit_list:
        divider = re.split(r"\s=\s", line)
        action = divider[0]
        value = divider[-1]
        if action == 'mask':
            total_mask = value
            # print(total_mask)
        else:
            # print action
            mem = re.findall(r"\d+", action)[0]
            binary_value = bin(int(value)).replace('0b', '')
            length_diff = len(total_mask) - len(binary_value)
            binary_value = '0' * length_diff + binary_value
            new_binary = []
            # print(binary_value)
            for c, b in enumerate(reversed(binary_value)):
                mask = total_mask[-(c+1)]
                if mask == 'X':
                    new_binary.insert(0, b)
                else:
                    new_binary.insert(0, mask)
            new_binary = ''.join(new_binary)
            total_sum_dict[mem] = int(new_binary, 2)
            # print(int(new_binary, 2))

    total_sum = 0
    for v in total_sum_dict.values():
        total_sum += v
    return total_sum


def parse(textData):
    bit_list = []
    for line in textData.splitlines():
        bit_list.append(line)
    return bit_list


def main():
    bit_list = []
    lines = ''
    with open('day14-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        bit_list = parse(lines)

    # print(solver_a(bit_list))
    print(solver_b(bit_list))


if __name__ == '__main__':
    main()
