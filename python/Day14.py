from typing import List


def apply_mask(value: int, mask: str) -> int:
    value_bin = format(value, '#036b')
    result = ''
    for i in range(0, 36):
        if mask[i] != 'X':
            result = result + mask[i]
        else:
            result = result + value_bin[i]
    return int(result, 2)


def apply_address_mask(address: int, mask: str) -> str:
    value_bin = format(address, '#038b')
    result = '0b'
    for i in range(2, 38):
        if mask[i - 2] != '0':
            result = result + mask[i - 2]
        else:
            result = result + value_bin[i]
    return result[2:]


def add_to_results(results_input: List[int], values: List[int]) -> List[int]:
    result_output = []
    if len(results_input) == 0:
        for value in values:
            result_output.append(value)
    else:
        for result_i in results_input:
            for value in values:
                result_output.append(result_i + value)
    return result_output


def demux_floating_address(floating_address: str) -> List[int]:
    results = []

    ltr_enum_address = [(pos, bit) for pos, bit in enumerate(reversed(floating_address))]

    for pos, bit in ltr_enum_address:
        if bit != 'X':
            results = add_to_results(results, [int(bit) * pow(2, pos)])
        else:
            results = add_to_results(results, [0 * pow(2, pos), 1 * pow(2, pos)])

    results.sort()
    return results


def main():
    mask = ''
    mem = {}
    with open('../input_day14_1.txt') as fp:
        for line in fp:
            if 'mask' in line:
                mask = line[7:].strip()
            else:
                l = line.strip().split(' = ')
                address = l[0][4:-1]
                value = l[1]
                mem[address] = apply_mask(int(value), mask)
        print(f'Result 1 is {sum(mem.values())}')

    mask = ''
    mem = {}
    with open('../input_day14_1.txt') as fp:
        for line in fp:
            if 'mask' in line:
                mask = line[7:].strip()
            else:
                l = line.strip().split(' = ')
                address = l[0][4:-1]
                value = l[1]

                address_list = demux_floating_address(apply_address_mask(int(address), mask))
                for address in address_list:
                    mem[address] = int(value)
        print(f'Result 2 is {sum(mem.values())}')


if __name__ == '__main__':
    main()
