def solver_a(bus_list):
    departure_time = bus_list[0]
    bus_schedule = bus_list[-1]
    departure_schedule_dict = {}
    buses = [int(bus) for bus in bus_schedule.split(',') if bus is not 'x']
    for bus in buses:
        departure_schedule_dict.setdefault(bus, [bus])
        while True:
            bus_departure_time = departure_schedule_dict[bus]
            bus_departure_time.append(bus_departure_time[-1] + bus)
            departure_schedule_dict[bus] = bus_departure_time
            if bus_departure_time[-2] + bus > departure_time:
                break
    wait_time = departure_time
    take_bus = ''
    for k, v in departure_schedule_dict.iteritems():
        # print departure_time, v[-1], v[-1] - departure_time
        if v[-1] - departure_time < wait_time:
            wait_time = v[-1] - departure_time
            take_bus = k

    return wait_time * take_bus


def solver_b(bus_list):
    # Brush up on Chinese remainder theorem
    # https://github.com/donth77/advent-of-code-2020/blob/main/day13/main.py
    bus_schedule = bus_list[-1]
    buses = [bus for bus in bus_schedule.split(',')]
    earliest_time = 0
    running_product = 1
    for (index, id) in enumerate(buses):
        if id == 'x':
            continue
        else:
            id = int(id)
        while((earliest_time + index) % id != 0):
            earliest_time += running_product
        running_product *= id
    return earliest_time


def parse(textData):
    bus_list = [int(textData.splitlines()[0])]
    bus_list.append(textData.splitlines()[-1])
    return bus_list


def main():
    bus_list = []
    lines = ''
    with open('day13-inputs.txt', 'r') as f:
        for line in f.readlines():
            lines += line
        bus_list = parse(lines)

    # print(solver_a(bus_list))
    print(solver_b(bus_list))


if __name__ == '__main__':
    main()
