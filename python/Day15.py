def main():
    input = [2, 0, 1, 9, 5, 19]
    result1 = compute_result1(input, 2020)
    print(f'Result1 is {result1}')
    result2 = compute_result1(input, 30000000)
    print(f'Result2 is {result2}')


def compute_result1(input, max_turn):
    game = {}
    for turn in range(1, len(input)):
        game[input[turn - 1]] = turn
    last = input[-1]

    for turn in range(len(input), max_turn):
        if last in game.keys():
            last_turn_spoken = game[last]
            game[last] = turn
            last = turn - last_turn_spoken
        else:
            game[last] = turn
            last = 0

    return last
if __name__ == '__main__':
    main()
