from time import process_time


class Day3:
    @staticmethod
    def computePosition(map, position, slope):
        if position['x'] + slope['x'] < len(map[0]):
            x_position = position['x'] + slope['x']
        else:
            x_position = (position['x'] + slope['x']) % len(map[0])

        return {'x': x_position, 'y': position['y'] + slope['y']}

    @staticmethod
    def isATree(map, position):
        return map[position['y']][position['x']] == 1

    @staticmethod
    def isFinish(map, position):
        return position['y'] >= len(map)-1

    @staticmethod
    def mapFromInput(fp):
        map = []
        for line in fp:
            line_map = []
            for caracter in line.strip():
                value = 1 if caracter == '#' else 0
                line_map.append(value)
            map.append(line_map)
        return map

    @staticmethod
    def howManyTrees(map, position, slope):
        current_position = position
        trees = 0
        while not Day3.isFinish(map, current_position):
            current_position = Day3.computePosition(map, current_position, slope)
            if Day3.isATree(map, current_position):
                trees += 1
        return trees

    @staticmethod
    def howManyTreesForSlopes(map, position, slopes):
        result = 1
        for slope in slopes:
            result *= Day3.howManyTrees(map, position, slope)
        return result


def main():

    with open('../input_day3_1.txt') as input_fp:

        position = {'x': 0, 'y': 0}
        slope = {'x': 3, 'y': 1}
        map = Day3.mapFromInput(input_fp)
        t = process_time()
        result_1 = Day3.howManyTrees(map, position, slope)
        print(f'Result 1 = {result_1} (in {process_time() - t}s)')

        t = process_time()
        slopes = [{'x': 1, 'y': 1},
                  {'x': 3, 'y': 1},
                  {'x': 5, 'y': 1},
                  {'x': 7, 'y': 1},
                  {'x': 1, 'y': 2}, ]
        result_2 = Day3.howManyTreesForSlopes(map, position, slopes)
        print(f'Result 2 = {result_2} (in {process_time() - t}s)')

if __name__ == '__main__':
    main()