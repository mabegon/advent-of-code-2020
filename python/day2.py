import re
from time import process_time


class Day2:
    @staticmethod
    def parseLine(line):
        m = re.match(r"(?P<number1>\d+)-(?P<number2>\d+) (?P<letter>.): (?P<password>\w+)", line)

        lineDict = m.groupdict()

        lineDict['number1'] = int(lineDict['number1'])
        lineDict['number2'] = int(lineDict['number2'])

        return lineDict

    @staticmethod
    def validatePasswordWithPolicyRules1(min_occurrences, max_occurences, letter, password):
        occurrences = password.count(letter)
        return occurrences >= min_occurrences and occurrences <= max_occurences

    @staticmethod
    def validatePasswordWithPolicyRules2(position1, position2, letter, password):
        letter1 = password[position1 - 1]
        letter2 = password[position2 - 1]
        return (letter1 == letter) != (letter2 == letter)


def main():
    input_path = '../input_day2_1.txt'
    number_valid_passwords_1 = 0
    number_valid_passwords_2 = 0
    t = process_time()
    with open(input_path) as input_fp:
        for line in input_fp:
            line_parsed = Day2.parseLine(line)
            valid_password_1 = Day2.validatePasswordWithPolicyRules1(line_parsed['number1'],
                                                                     line_parsed['number2'],
                                                                     line_parsed['letter'],
                                                                     line_parsed['password'])
            if valid_password_1:
                number_valid_passwords_1 += 1

            valid_password_2 = Day2.validatePasswordWithPolicyRules2(line_parsed['number1'],
                                                                     line_parsed['number2'],
                                                                     line_parsed['letter'],
                                                                     line_parsed['password'])
            if valid_password_2:
                number_valid_passwords_2 += 1
    print(f'Process Time {process_time() - t}s')
    print(f'Number of Valid Passwords 1 is {number_valid_passwords_1}')
    print(f'Number of Valid Passwords 2 is {number_valid_passwords_2}')


if __name__ == '__main__':
    main()
