WEST = 270
SOUTH = 180
EAST = 90
NORTH = 0
LEFT = -1
RIGHT = 1
FACING_WEST = 'west'
FACING_SOUTH = 'south'
FACING_EAST = 'east'
FACING_NORTH = 'north'
NORTH_SOUTH = 'north_south'
EAST_WEST = 'east_west'
ORIENTED = 'Oriented'


def decode_command(command: str):
    action = command[0]
    value = int(command[1:])
    return action, value


def compute_state(state: dict, command: str) -> dict:
    action, value = decode_command(command)
    if action == 'F':
        return forward_action(state, value)
    elif action == 'W':
        return west_action(state, value)
    elif action == 'E':
        return east_action(state, value)
    elif action == 'N':
        return north_action(state, value)
    elif action == 'S':
        return south_action(state, value)
    elif action == 'L':
        return rotate_left_action(state, value)
    elif action == 'R':
        return rotate_right_action(state, value)
    return None


def get_facing(degrees: int) -> str:
    if degrees == NORTH:
        return FACING_NORTH
    elif degrees == EAST:
        return FACING_EAST
    elif degrees == SOUTH:
        return FACING_SOUTH
    elif degrees == WEST:
        return FACING_WEST
    else:
        return None


def forward_action(state: dict, value: int) -> dict:
    facing = get_facing(state[ORIENTED])

    if facing == FACING_EAST:
        return east_action(state, value)
    elif facing == FACING_WEST:
        return west_action(state, value)
    elif facing == FACING_NORTH:
        return north_action(state, value)
    elif facing == FACING_SOUTH:
        return south_action(state, value)


def west_action(state, value):
    new_state = state.copy()
    new_state[EAST_WEST] -= value
    return new_state


def east_action(state, value):
    new_state = state.copy()
    new_state[EAST_WEST] += value
    return new_state


def north_action(state, value):
    new_state = state.copy()
    new_state[NORTH_SOUTH] += value
    return new_state


def south_action(state, value):
    new_state = state.copy()
    new_state[NORTH_SOUTH] -= value
    return new_state


def rotate_left_action(state, degrees):
    new_state = state.copy()
    if new_state[ORIENTED] - abs(degrees) % 360 >= 0:
        new_state[ORIENTED] -= abs(degrees) % 360
    else:
        new_state[ORIENTED] = 360 - abs(new_state[ORIENTED] - degrees) % 360
    if new_state[ORIENTED] == 360:
        new_state[ORIENTED] = 0
    return new_state


def rotate_right_action(state, degrees):
    new_state = state.copy()
    if new_state[ORIENTED] + abs(degrees) % 360 > 360:
        new_state[ORIENTED] = 0 + abs(new_state[ORIENTED] + degrees) % 360
    else:
        new_state[ORIENTED] += abs(degrees) % 360

    if new_state[ORIENTED] == 360:
        new_state[ORIENTED] = 0
    return new_state


def compute_result1(state, commands):
    current_state = state
    for command in commands:
        current_state = compute_state(current_state, command)
    return abs(current_state[NORTH_SOUTH]) + abs(current_state[EAST_WEST])


def main():
    commands = []
    state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 0}

    with open('../input_day12_1.txt') as fp:
        for line in fp:
            commands.append(line.strip())
    result1 = compute_result1(state, commands)
    print(f'Result 1 is {result1}')


if __name__ == '__main__':
    main()
