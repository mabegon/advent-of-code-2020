def count_adjacent_occupied(board, position):
    count = 0
    column = position[0]
    row = position[1]

    col1 = column - 1 if column - 1 >= 0 else column
    col2 = column + 1 if column + 1 < len(board[row]) else column
    row1 = row - 1 if row - 1 >= 0 else row
    row2 = row + 1 if row + 1 < len(board) else row

    for current_row in range(row1, row2 + 1):
        for current_column in range(col1, col2 + 1):
            if (current_column != column or current_row != row) and board[current_row][current_column] == '#':
                count += 1
    return count


def must_occupy_seat(board, position):
    x = position[0]
    y = position[1]

    return board[y][x] == 'L' and count_adjacent_occupied(board, position) == 0


def must_free_seat(board, position):
    x = position[0]
    y = position[1]

    return board[y][x] == '#' and count_adjacent_occupied(board, position) >= 4


def compute_movement(board):
    new_board = []
    for y in range(0, len(board)):
        new_line = []
        for x in range(0, len(board[0])):
            value = board[y][x]
            if value == 'L':
                if must_occupy_seat(board, (x, y)):
                    new_line.append('#')
                else:
                    new_line.append('L')
            elif value == '#':
                if must_free_seat(board, (x, y)):
                    new_line.append('L')
                else:
                    new_line.append('#')
            else:
                new_line.append('.')
        new_board.append(new_line)
    return new_board


def parse_board(fp):
    board = []
    for line in fp:
        line_list = [char for char in line.strip()]
        board.append(line_list)
    return board


def find_stable_state(board):
    current_board = None
    new_board = board
    while current_board != new_board:
        current_board = new_board
        new_board = compute_movement(current_board)
    return new_board


def compute_result1(board):
    stable_board = find_stable_state(board)
    result = count_occupied_on_board(stable_board)
    return result


def count_occupied_on_board(stable_board):
    result = 0
    for line in stable_board:
        result += line.count('#')
    return result


def main():
    with open('../input_day11_1.txt') as fp:
        board = parse_board(fp)
        result1 = compute_result1(board)
        print(f'Result 1 is {result1}')


if __name__ == '__main__':
    main()
