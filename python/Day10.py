def parse_input(fp):
    adapters = []
    for line in fp:
        adapters.append(int(line.strip()))
    return adapters

def device_joltage(adapters):
    return max(adapters)+3


def select_best_adapter(adapters, rating):
    candidates = [adapter for adapter in adapters if adapter > rating and adapter <= rating+3]
    return min(candidates)

def compute_result1(adapters):
    differences = []
    dj = device_joltage(adapters)
    current_joltage = 0
    while current_joltage < dj-3:
        adapter_selected = select_best_adapter(adapters, current_joltage)
        differences.append(adapter_selected-current_joltage)
        current_joltage = adapter_selected
    differences.append(dj-current_joltage)
    return differences.count(1)*differences.count(3)



def main():
    with open('../input_day10_1.txt') as fp:
        adapters = parse_input(fp)
        result1 = compute_result1(adapters)
        print(f'Result 1 is {result1}')

if __name__ == '__main__':
    main()