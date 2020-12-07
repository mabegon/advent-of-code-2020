import re


def parse_line(line):
    occurrences = re.findall('(\d)?\s?(\w+\s\w+)\sbag', line)
    values = {}
    key = ''
    for occurrence in occurrences:
       if occurrence[0] != '':
           values[occurrence[1]] = int(occurrence[0])
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


def compute_question_1(rules, bag):
    who_can_hold_dict = who_can_hold_by_rules(rules)
    result = who_can_hold(bag, who_can_hold_dict)
    return len(result)

def get_rules(fp):
    rules = {}
    for line in fp:
        key, values = parse_line(line)
        rules[key] = values
    return rules


def count_bags(bag, rules):
    result = 0
    if bag not in rules.keys() or rules[bag] is None:

        return 0
    else:
        content_bags = rules[bag]
        for content_bag in content_bags.keys():
            result += content_bags[content_bag] * count_bags(content_bag, rules)
            result += content_bags[content_bag]
    return result

def compute_question_2(rules, bag):
    return count_bags(bag, rules)


def main():
    with open('../input_day7_1.txt') as fp:
        rules = get_rules(fp)
        result_1 = compute_question_1(rules, 'shiny gold')
        print(f'Result 1 is {result_1}')
        result_2 = compute_question_2(rules, 'shiny gold')
        print(f'Result 2 is {result_2}')


if __name__ == '__main__':
    main()
