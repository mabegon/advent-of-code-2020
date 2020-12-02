import re
from time import process_time


class Day2:
    @staticmethod
    def parseLine(line):
        m = re.match(r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>.): (?P<password>\w+)", line)

        lineDict = m.groupdict()

        lineDict['min'] = int(lineDict['min'])
        lineDict['max'] = int(lineDict['max'])

        return lineDict

    @staticmethod
    def validatePassword(min_occurrences, max_occurences, letter, password):
        occurrences = password.count(letter)
        return occurrences >= min_occurrences and occurrences <= max_occurences


def main():
    input_path = './input_day2_1.txt'
    number_valid_passwords = 0
    t = process_time()
    with open(input_path) as input_fp:
        for line in input_fp:
            line_parsed = Day2.parseLine(line)
            valid_password = Day2.validatePassword(line_parsed['min'],
                                          line_parsed['max'],
                                          line_parsed['letter'],
                                          line_parsed['password'])
            if valid_password:
                number_valid_passwords += 1
    print(f'Number of Valid Passwords is {number_valid_passwords} (in {process_time() - t}s)')


if __name__ == '__main__':
    main()
