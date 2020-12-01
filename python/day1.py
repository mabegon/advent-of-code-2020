input_path = './input_day1_1.txt'

class Day1():
    @staticmethod
    def foundTwoEntries(input):
        for entry1 in input:
            for entry2 in input:
                if entry1 != entry2 and ((entry1 + entry2) == 2020):
                    return [entry1, entry2]
        return [None]

    @staticmethod
    def foundThreeEntries(input):
        for entry1 in input:
            for entry2 in input:
                if entry1 != entry2:
                    for entry3 in input:
                        if entry1 != entry3 and entry2 != entry3 and ((entry1 + entry2+ entry3) == 2020):
                            return [entry1, entry2, entry3]
        return [None]
    @staticmethod
    def computeResult1_1(entry_list):
        return entry_list[0] * entry_list[1]

    @staticmethod
    def computeResult1_2(entry_list):
        return entry_list[0] * entry_list[1] * entry_list[2]

def main():
    input1 = []
    with open(input_path) as input_fp:
        for entry_input in input_fp:
            input1.append(int(entry_input))

    result_1 = Day1.computeResult1_1(Day1.foundTwoEntries(input1))
    result_2 = Day1.computeResult1_2(Day1.foundThreeEntries(input1))
    print(f'Result 1 = {result_1}')
    print(f'Result 2 = {result_2}')


if __name__ == '__main__':
    main()
