from unittest import TestCase

from python.Day3 import Day3


class TestDay3(TestCase):

    def test_must_be_move_inside_map(self):
        map = [[0, 0],
               [0, 0]]
        position = {'x': 0, 'y': 0}
        slope = {'x': 1, 'y': 1}

        new_position = Day3.computePosition(map, position, slope)

        self.assertEqual({'x': 1, 'y': 1}, new_position)

    def test_must_be_accept_x_overflow(self):
        map = [[0, 0],
               [0, 0]]
        position = {'x': 0, 'y': 0}
        slope = {'x': 2, 'y': 1}

        new_position = Day3.computePosition(map, position, slope)

        self.assertEqual({'x': 0, 'y': 1}, new_position)

    def test_must_be_accept_x_double_overflow(self):
        map = [[0, 0],
               [0, 0]]
        position = {'x': 0, 'y': 0}
        slope = {'x': 4, 'y': 1}

        new_position = Day3.computePosition(map, position, slope)

        self.assertEqual({'x': 0, 'y': 1}, new_position)

    def test_must_be_true_if_position_is_a_tree(self):
        map = [[1, 0],
               [0, 0]]
        position = {'x': 0, 'y': 0}

        self.assertTrue(Day3.isATree(map, position))

    def test_must_be_False_if_position_is_not_a_tree(self):
        map = [[1, 0],
               [0, 0]]
        position = {'x': 1, 'y': 0}

        self.assertFalse(Day3.isATree(map, position))

    def test_must_be_true_if_position_y_is_bottom(self):
        map = [[1, 0],
               [0, 0]]
        position = {'x': 0, 'y': 1}

        self.assertTrue(Day3.isFinish(map, position))

    def test_must_be_False_if_position_y_is_not_bottom(self):
        map = [[1, 0],
               [0, 0]]
        position = {'x': 0, 'y': 0}

        self.assertFalse(Day3.isFinish(map, position))

    def test_populate_Map(self):
        expected_map = [[0, 0, 1, 1, 0],
                        [1, 0, 0, 0, 1]]
        with open('./input_test_day3_b.txt') as input_fp:
            map = Day3.mapFromInput(input_fp)
            self.assertEqual(expected_map, map)

    def test_exemple_from_Question_1(self):
        position = {'x': 0, 'y': 0}
        slope = {'x': 3, 'y': 1}

        with open('./input_test_day3.txt') as input_fp:
            self.assertEqual(7, Day3.howManyTrees(input_fp, position, slope))