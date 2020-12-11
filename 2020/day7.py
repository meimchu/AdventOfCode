from aoc_timer import time_it
import re


class BagExamine():
    def __init__(self, bag_dict):
        self._bag_dict = bag_dict
        self._total_occurence = 0
        self._search_bag = ''
        self._occured_set = set()
        self._occured_dict = {}

    @property
    def bag_dict(self):
        return self._bag_dict

    @property
    def total_occurence(self):
        return len(self.occured_set)

    @property
    def search_bag(self):
        return self._search_bag

    @property
    def occured_set(self):
        return self._occured_set

    @property
    def occured_dict(self):
        return self._occured_dict

    def search_occurence(self, bag_name):
        self.search_bag = bag_name

        for k, v in self.bag_dict.iteritems():
            bag_list = []
            if k != self.search_bag:
                for item in v:
                    name_contains = item[-1]
                    bag_list.append(name_contains)

            if self.search_bag in bag_list:
                self.occured_set.add(k)
            else:
                for item in bag_list:
                    self.search_recursion(item, k)

        return self.total_occurence

    def search_recursion(self, bag_name, original_bag):
        bag_list = []
        for item in self.bag_dict.get(bag_name):
            name_contains = item[1]
            bag_list.append(name_contains)

        if self.search_bag in bag_list:
            self.occured_set.add(original_bag)
        else:
            for item in bag_list:
                self.search_recursion(item, original_bag)

    def search_contain(self, bag_name):
        self.search_contain_recursion(bag_name)
        total = 0
        for v in self.occured_dict.values():
            total += v
        return total

    def search_contain_recursion(self, bag_name, parent_num=1):
        for item in self.bag_dict.get(bag_name):
            num_contains = int(item[0])
            total_num = parent_num * num_contains
            name_contains = item[1]
            try:
                self.occured_dict[name_contains] += total_num
            except KeyError:
                self.occured_dict[name_contains] = total_num
            self.search_contain_recursion(name_contains, total_num)


@time_it
def solver_a(bagList):
    bag_dict = {}
    for line in bagList:
        bags = re.findall(
            r"([0-9]{1,})\s([a-zA-Z]*\s[a-zA-Z]*)", line)
        bag_key = ' '.join(line.split(' ')[:2])
        bag_dict[bag_key] = bags
    bag_obj = BagExamine(bag_dict)

    return bag_obj.search_occurence('shiny gold')


@time_it
def solver_b(bag_list):
    bag_dict = {}
    for line in bag_list:
        bags = re.findall(
            r"(?P<num>[0-9]{1,})\s(?P<name>[a-zA-Z]*\s[a-zA-Z]*)", line)
        bag_key = re.match(r"^\w*\s\w*", line)
        bag_dict[bag_key.group()] = bags
    bag_obj = BagExamine(bag_dict)

    return bag_obj.search_contain('shiny gold')


def parse(textData):
    bag_list = []
    for line in textData.splitlines():
        bag_list.append(line)
    return bag_list

def main():
    bag_list = []
    lines = ''
    with open('day7-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        bag_list = parse(lines)

    print(solver_a(bag_list))
    print(solver_b(bag_list))


if __name__ == '__main__':
    main()
