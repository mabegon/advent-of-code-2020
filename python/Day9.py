def check_validity(numbers, current_number_position, preamble):
    current_number = numbers[current_number_position]
    selected_numbers_positions = range(current_number_position - preamble, current_number_position)
    sums = set()
    for number_position1 in selected_numbers_positions:
        for number_position2 in selected_numbers_positions:
            if number_position1 != number_position2:
                sums.add(numbers[number_position1]+numbers[number_position2])

    if current_number in sums:
        return True
    else:
        return False

def parse_input(fp):
    numbers = []
    for line in fp:
        numbers.append(int(line))
    return numbers

def find_first_wrong_number(numbers, preamble):
    for position in range(preamble, len(numbers)):
        if not check_validity(numbers, position, preamble):
            return numbers[position]
    return None

def compute_result_1(fp, preamble):
        numbers = parse_input(fp)
        result1 = find_first_wrong_number(numbers, preamble)
        return result1

def main():
    preamble = 25
    with open('../input_day9_1.txt') as fp:
        result1 = compute_result_1(fp, preamble)
        print(f'First wrong number is {result1}')

if __name__ == '__main__':
    main()


