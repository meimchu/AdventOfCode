from __future__ import absolute_import


def solver_a(bit_list):
    bit_dict = {}
    for bits in bit_list:
        for i, bit in enumerate(bits):
            if i not in bit_dict:
                bit_dict[i] = 0
            if bit == '1':
                bit_dict[i] += 1

    gamma_rate = []
    epsilon_rate = []
    for k, v in bit_dict.items():
        if v > len(bit_list) // 2:
            gamma_rate.append('1')
            epsilon_rate.append('0')
        else:
            epsilon_rate.append('1')
            gamma_rate.append('0')

    gamma_dec = int(''.join(gamma_rate), 2)
    epsilon_dec = int(''.join(epsilon_rate), 2)

    return gamma_dec * epsilon_dec


def solver_b(bit_list):
    bit_dict = {}
    for bits in bit_list:
        for i, bit in enumerate(bits):
            if i not in bit_dict:
                bit_dict[i] = 0
            if bit == '1':
                bit_dict[i] += 1

    accepted_oxygen_list = bit_list.copy()

    for i in range(len(accepted_oxygen_list[0])):
        digit_list = []
        for m in accepted_oxygen_list:
            digit_list.append(int(m[i]))

        if sum(digit_list) > len(digit_list) // 2:
            most_common = '1'
        elif sum(digit_list) == len(digit_list) / 2:
            most_common = '1'
        else:
            most_common = '0'

        count = len(accepted_oxygen_list) - 1
        while count >= 0:
            if accepted_oxygen_list[count][i] != most_common:
                accepted_oxygen_list.pop(count)
            count -= 1

        if len(accepted_oxygen_list) == 1:
            break

    accepted_carbon_two_rate = bit_list.copy()
    for i in range(len(accepted_carbon_two_rate[0])):
        digit_list = []
        for m in accepted_carbon_two_rate:
            digit_list.append(int(m[i]))

        if sum(digit_list) > len(digit_list) // 2:
            least_common = '0'
        elif sum(digit_list) == len(digit_list) / 2:
            least_common = '0'
        else:
            least_common = '1'

        count = len(accepted_carbon_two_rate) - 1
        while count >= 0:
            if accepted_carbon_two_rate[count][i] != least_common:
                accepted_carbon_two_rate.pop(count)
            count -= 1

        if len(accepted_carbon_two_rate) == 1:
            break

    oxygen_dec = int(''.join(accepted_oxygen_list[0]), 2)
    carbon_two_dec = int(''.join(accepted_carbon_two_rate[0]), 2)

    return oxygen_dec * carbon_two_dec


def generate_list(string=None):
    bit_list = []

    if string is None:
        with open('day3-inputs.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                bit_list.append(line)
    else:
        for line in string.split('\n'):
            bit_list.append(line)

    return bit_list


def main():
    bit_list = generate_list()

    print(solver_a(bit_list))
    print(solver_b(bit_list))


if __name__ == '__main__':
    main()
