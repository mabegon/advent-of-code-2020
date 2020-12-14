import itertools


def find_first_bus(bus_list, earliest_bus):
    for time in itertools.count(start=earliest_bus):
        for bus in bus_list:
            if time % bus == 0:
                return bus, time - earliest_bus


def main():
    with open('../input_day13_1.txt') as fp:
        earliest_bus = int(fp.readline().strip())
        bus_str = fp.readline().strip()
        bus_list = []
        for element in bus_str.split(','):
            if element != 'x':
                bus_list.append(int(element))
        print(bus_list)
        bus, minutes = find_first_bus(bus_list, earliest_bus)

        print(f'Result 1 for bus n. {bus} and waiting {minutes} minutes,  is {bus * minutes}')


if __name__ == '__main__':
    main()
