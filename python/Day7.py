import re


def parse_line(line):
    occurrences = re.findall('(\d)?\s?(\w+\s\w+)\sbag', line)
    values = {}
    key = ''
    for occurrence in occurrences:
       if occurrence[0] != '':
           values[occurrence[1]] = occurrence[0]
       else:
           key = occurrence[1]
    return key, values


def who_can_hold_by_rule(container_bag, content_bags):
    # {'light red': { 'bright white': '1', 'muted yellow': '2'}}
    result = {}
    #container_bag = [element for element in rule.keys() if rule[element] == 'container'][0]
    #content_bags = [element for element in rule.keys() if rule[element] != 'container']
    for bag in content_bags:
        result[bag] = container_bag
    return result


def who_can_hold_by_rules(rules):
    who_dict_consolidated = {}
    for rule_key in rules.keys():

        who_by_rule = who_can_hold_by_rule(rule_key, rules[rule_key])
        for bag in who_by_rule.keys():
            if bag not in who_dict_consolidated.keys():
                who_dict_consolidated[bag] = [who_by_rule[bag]]
            else:
                who_dict_consolidated[bag].append(who_by_rule[bag])
    return who_dict_consolidated


def who_can_hold(input_bag, dict):
    result = set()
    if input_bag in dict.keys():
        for bag in dict[input_bag]:
            result.add(bag)
            result = result.union(who_can_hold(bag, dict))
    return result


def compute_question_1(fp, bag):
    rules ={}
    for line in fp:
        key, values = parse_line(line)
        rules[key] = values
    who_can_hold_dict = who_can_hold_by_rules(rules)
    result = who_can_hold(bag, who_can_hold_dict)
    return len(result)

def main():
    with open('../input_day7_1.txt') as fp:
        result_1 = compute_question_1(fp, 'shiny gold')
        print(f'Result 1 is {result_1}')


if __name__ == '__main__':
    main()