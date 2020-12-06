import math


def count_yes_groups(fp):
    groups = []
    group = set()
    for line in fp:
        if line.strip() == '':
            groups.append(len(group))
            group = set()
        else:
            for yes in line.strip():
                group.add(yes)

    groups.append(len(group))
    return groups


def count_yes_intersections_groups(fp):
    groups = []
    group = {}
    members = 0
    for line in fp:
        if line.strip() == '':
            groups.append(len([question for question in group.keys() if group[question] == members]))
            group = {}
            members = 0
        else:
            members += 1
            for question in line.strip():
                group[question] = group[question] + 1 if question in group else 1
    groups.append(len([question for question in group.keys() if group[question] == members]))
    return groups


def compute_result(fp):
    groups = count_yes_groups(fp)
    return sum(groups)


def compute_result2(fp):
    groups = count_yes_intersections_groups(fp)
    return sum(groups)


def main():
    with open('../input_day6_1.txt') as input_fp:
        result = compute_result(input_fp)
        print(f'Le resultat 1 est {result}')
    with open('../input_day6_1.txt') as input_fp:
        result2 = compute_result2(input_fp)
        print(f'Le resultat 2 est {result2}')


if __name__ == '__main__':
    main()
