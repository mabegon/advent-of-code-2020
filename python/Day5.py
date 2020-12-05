import math

LEFT = 'L'
FRONT = 'F'


def select_partition(min, max, action):
    distance = (max - min) / 2
    if action in [FRONT, LEFT]:
        return min, math.floor(max - distance)
    else:
        return math.ceil(min + distance), max


def select_row(actions):
    min = 0
    max = 127
    for action in actions:
        min, max = select_partition(min, max, action)

    if min != max:
        print(f'Alerte: min {min} et max {max} sont differents')
    return min


def select_column(actions):
    min = 0
    max = 7
    for action in actions:
        min, max = select_partition(min, max, action)

    if min != max:
        print(f'Alerte: min {min} et max {max} sont differents')
    return min


def select_seat(actions):
    row = select_row(actions[:7])
    column = select_column(actions[7:])
    return row * 8 + column


def find_my_seat(seats):
    for seat in sorted(seats):
        if seat + 1 not in seats and seat + 2 in seats:
            return seat + 1


def main():
    highest_seat = 0
    seats = []
    with open('../input_day5_1.txt') as input_fp:
        for actions in input_fp:
            seat = select_seat(actions.strip())
            seats.append(seat)
            highest_seat = seat if seat > highest_seat else highest_seat
    my_seat = find_my_seat(seats)
    print(f'The highest seat ID is {highest_seat}')
    print(f'My seat is  is {my_seat}')


if __name__ == '__main__':
    main()
