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


def compute_result(fp):
    groups = count_yes_groups(fp)
    return sum(groups)


def main():
    with open('../input_day6_1.txt') as input_fp:
        result = compute_result(input_fp)
        print(f'Le resultat 1 est {result}')


if __name__ == '__main__':
    main()
