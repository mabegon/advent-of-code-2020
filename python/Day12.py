WAYPOINT_EAST_WEST = 'waypoint_east_west'
WAYPOINT_NORTH_SOUTH = 'waypoint_north_south'
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
    new_state[ORIENTED] = rotate_left(degrees, new_state[ORIENTED])
    return new_state


def rotate_left(degrees, origin):
    if origin - abs(degrees) % 360 >= 0:
        result = origin - abs(degrees) % 360
    else:
        result = 360 - abs(origin - degrees) % 360
    if result == 360:
        result = 0
    return result


def rotate_right_action(state, degrees):
    new_state = state.copy()
    new_state[ORIENTED] = rotate_right(degrees, new_state[ORIENTED])
    return new_state


def rotate_right(degrees, origin):
    if origin + abs(degrees) % 360 > 360:
        result = 0 + abs(origin + degrees) % 360
    else:
        result = origin + abs(degrees) % 360
    if result == 360:
        result = 0
    return result


def compute_result1(state, commands):
    current_state = state
    for command in commands:
        current_state = compute_state(current_state, command)
    return abs(current_state[NORTH_SOUTH]) + abs(current_state[EAST_WEST])


def compute_result2(state, commands):
    current_state = state
    for command in commands:
        current_state = compute_state_v2(current_state, command)
    return abs(current_state[NORTH_SOUTH]) + abs(current_state[EAST_WEST])


def forward_action_v2(state: dict, value: int) -> dict:
    new_state = state.copy()
    new_state[NORTH_SOUTH] += state[WAYPOINT_NORTH_SOUTH] * value
    new_state[EAST_WEST] += state[WAYPOINT_EAST_WEST] * value
    return new_state


def west_action_v2(state, value):
    new_state = state.copy()
    new_state[WAYPOINT_EAST_WEST] -= value
    return new_state


def east_action_v2(state, value):
    new_state = state.copy()
    new_state[WAYPOINT_EAST_WEST] += value
    return new_state


def north_action_v2(state, value):
    new_state = state.copy()
    new_state[WAYPOINT_NORTH_SOUTH] += value
    return new_state


def south_action_v2(state, value):
    new_state = state.copy()
    new_state[WAYPOINT_NORTH_SOUTH] -= value
    return new_state


def rotate_action(state, degrees, rotate_strategy):
    new_state = state.copy()

    degrees_north_south = 0 if new_state[WAYPOINT_NORTH_SOUTH] > 0 else 180
    degrees_east_west = 90 if new_state[WAYPOINT_EAST_WEST] > 0 else 270

    new_degrees_north_south = rotate_strategy(degrees, degrees_north_south)
    new_degrees_east_west = rotate_strategy(degrees, degrees_east_west)

    if new_degrees_north_south == 0:
        new_state[WAYPOINT_NORTH_SOUTH] = abs(state[WAYPOINT_NORTH_SOUTH])
    elif new_degrees_north_south == 90:
        new_state[WAYPOINT_EAST_WEST] = abs(state[WAYPOINT_NORTH_SOUTH])
    elif new_degrees_north_south == 180:
        new_state[WAYPOINT_NORTH_SOUTH] = abs(state[WAYPOINT_NORTH_SOUTH]) * -1
    elif new_degrees_north_south == 270:
        new_state[WAYPOINT_EAST_WEST] = abs(state[WAYPOINT_NORTH_SOUTH]) * -1

    if new_degrees_east_west == 0:
        new_state[WAYPOINT_NORTH_SOUTH] = abs(state[WAYPOINT_EAST_WEST])
    elif new_degrees_east_west == 90:
        new_state[WAYPOINT_EAST_WEST] = abs(state[WAYPOINT_EAST_WEST])
    elif new_degrees_east_west == 180:
        new_state[WAYPOINT_NORTH_SOUTH] = abs(state[WAYPOINT_EAST_WEST]) * -1
    elif new_degrees_east_west == 270:
        new_state[WAYPOINT_EAST_WEST] = abs(state[WAYPOINT_EAST_WEST]) * -1

    return new_state


def compute_state_v2(state: dict, command: str) -> dict:
    action, value = decode_command(command)
    if action == 'F':
        return forward_action_v2(state, value)
    elif action == 'W':
        return west_action_v2(state, value)
    elif action == 'E':
        return east_action_v2(state, value)
    elif action == 'N':
        return north_action_v2(state, value)
    elif action == 'S':
        return south_action_v2(state, value)
    elif action == 'L':
        return rotate_left_action_v2(state, value)
    elif action == 'R':
        return rotate_right_action_v2(state, value)
    return None


def rotate_right_action_v2(state, value):
    return rotate_action(state, value, rotate_right)


def rotate_left_action_v2(state, value):
    return rotate_action(state, value, rotate_left)

def main():
    commands = []
    state = {ORIENTED: EAST, NORTH_SOUTH: 0, EAST_WEST: 0}

    with open('../input_day12_1.txt') as fp:
        for line in fp:
            commands.append(line.strip())
    result1 = compute_result1(state, commands)
    print(f'Result 1 is {result1}')

    state_v2 = {WAYPOINT_NORTH_SOUTH: 1, WAYPOINT_EAST_WEST: 10, NORTH_SOUTH: 0, EAST_WEST: 0}
    result2 = compute_result2(state_v2, commands)
    print(f'Result 2 is {result2}')


if __name__ == '__main__':
    main()
