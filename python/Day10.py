from functools import cache, lru_cache


def parse_input(fp):
    adapters = []
    for line in fp:
        adapters.append(int(line.strip()))
    return adapters


def device_joltage(adapters):
    return max(adapters) + 3


def select_best_adapter(adapters, joltage):
    candidates = adapter_candidates(adapters, joltage)
    return min(candidates)


def adapter_candidates(adapters, joltage):
    return [adapter for adapter in adapters if adapter > joltage and adapter <= joltage + 3]


def compute_result1(adapters):
    differences = []
    dj = device_joltage(adapters)
    current_joltage = 0
    while current_joltage < dj - 3:
        adapter_selected = select_best_adapter(adapters, current_joltage)
        differences.append(adapter_selected - current_joltage)
        current_joltage = adapter_selected
    differences.append(dj - current_joltage)
    return differences.count(1) * differences.count(3)


def how_many_ways(adapters, current_joltage, target_joltage):
    if current_joltage >= target_joltage - 3:
        return 1
    else:
        candidates = adapter_candidates(adapters, current_joltage)
        result = 0
        for candidate in candidates:
            adapters_updated = list(adapters.copy())
            adapters_updated.remove(candidate)
            result += how_many_ways(adapters_updated, candidate, target_joltage)
        return result


def compute_result2(adapters):
    current_joltage = 0
    target_joltage = device_joltage(adapters)
    adapters.sort()
    return how_many_ways(adapters, current_joltage, target_joltage)


def main():
    with open('../input_day10_1.txt') as fp:
        adapters = parse_input(fp)
        result1 = compute_result1(adapters)
        print(f'Result 1 is {result1}')
        result2 = compute_result2(adapters)
        print(f'Result 2 is {result2}')


if __name__ == '__main__':
    main()
