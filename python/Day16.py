import re


def add_rule(rules_input: dict, line: str) -> dict:

    rules = rules_input.copy()
    m = re.match(r"(?P<name>.+): (?P<range1str>\d+-\d+) or (?P<range2str>\d+-\d+)", line.strip())

    lineDict = m.groupdict()
    range1 = lineDict['range1str'].split('-')
    for i in range(int(range1[0]), int(range1[1])+1):
        if i in rules.keys():
            rules[i].append(lineDict['name'])
        else:
            rules[i] = [lineDict['name']]

    range2 = lineDict['range2str'].split('-')
    for i in range(int(range2[0]), int(range2[1])+1):
        if i in rules.keys():
            rules[i].append(lineDict['name'])
        else:
            rules[i] = [lineDict['name']]

    return rules


def ticket_error_rate(line: str, rules: dict) -> int:
    for field in line.split(','):
        if int(field) not in rules.keys():
            return int(field)
    return 0

def compute_result1(fp):
    bloc = 'rules'
    rules = {}
    your_ticket = ''
    error_rate = 0
    for line in fp:
        if bloc == 'rules':
            if line.strip() == '':
                bloc = 'your_ticket'
            else:
                rules = add_rule(rules, line.strip())
        elif bloc == 'your_ticket':
            if line.strip() == '':
                bloc = 'nearby_tickets'
            elif line.strip() == 'your ticket:':
                pass
            else:
                your_ticket = line.strip()
        else:
            if line.strip() == 'nearby tickets:':
                pass
            else:
                error_rate += ticket_error_rate(line.strip(), rules)
    return error_rate

def main():
    with open('../input_day16_1.txt') as fp:
        result1 = compute_result1(fp)
        print(f'Result1 is {result1}')

if __name__ == '__main__':
    main()