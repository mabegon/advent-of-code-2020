import itertools
from typing import Tuple, List


def find_first_bus(bus_list, earliest_bus):
    for time in itertools.count(start=earliest_bus):
        for bus in bus_list:
            if time % bus == 0:
                return bus, time - earliest_bus


def transform_input(bus_str: str):
    return [(int(b), i) for i, b in enumerate(bus_str.split(',')) if b != 'x']


def find_earliest_timestamp(bus_offsets: List[Tuple[int, int]]) -> int:
    timestamp_step = bus_offsets[0][0]
    t = timestamp_step
    for bus, time_offset in bus_offsets[1:]:
        while (t + time_offset) % bus != 0:
            t += timestamp_step
        timestamp_step *= bus
    return t


def main():
    with open('../input_day13_1.txt') as fp:
        earliest_bus = int(fp.readline().strip())
        bus_str = fp.readline().strip()
        bus_list = []
        for element in bus_str.split(','):
            if element != 'x':
                bus_list.append(int(element))
        bus, minutes = find_first_bus(bus_list, earliest_bus)
        print(f'Result 1 for bus n. {bus} and waiting {minutes} minutes,  is {bus * minutes}')

        bus_offsets = transform_input(bus_str)
        earliest_timestamp = find_earliest_timestamp(bus_offsets)
        print(f'The earliest timestamp is {earliest_timestamp}')


if __name__ == '__main__':
    main()
