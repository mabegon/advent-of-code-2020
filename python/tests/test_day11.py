from unittest import TestCase
import python.Day11


class TestDay11(TestCase):
    def test_count_adjacents_must_be_0(self):
        board = [['L', 'L', 'L'],
                 ['L', 'L', 'L'],
                 ['L', 'L', 'L']]
        position = (1, 1)

        self.assertEqual(0, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_0_also(self):
        board = [['L', 'L', 'L'],
                 ['L', '#', 'L'],
                 ['L', 'L', 'L']]
        position = (1, 1)

        self.assertEqual(0, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_2(self):
        board = [['L', 'L', '#'],
                 ['L', '#', 'L'],
                 ['#', 'L', 'L']]
        position = (1, 1)

        self.assertEqual(2, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_3(self):
        board = [['L', '#', '#'],
                 ['#', '#', 'L'],
                 ['#', 'L', 'L']]
        position = (0, 0)

        self.assertEqual(3, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_1(self):
        board = [['L', '#', '#'],
                 ['#', '#', 'L'],
                 ['#', 'L', 'L']]
        position = (2, 2)

        self.assertEqual(1, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_3_for_position_2_2(self):
        board = [['L', '#', '#'],
                 ['#', '#', '#'],
                 ['#', '#', '#']]
        position = (2, 2)

        self.assertEqual(3, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_5_for_position_2_1(self):
        board = [['L', '#', '#'],
                 ['#', '#', '#'],
                 ['#', '#', '#']]
        position = (2, 1)

        self.assertEqual(5, python.Day11.count_adjacent_occupied(board, position))

    def test_count_adjacents_must_be_5_for_position_4_2(self):
        board = [['L', '#', '#', 'L', '#', '#'],
                 ['#', 'L', '#', 'L', '#', 'L'],
                 ['#', 'L', 'L', '#', 'L', '#'],
                 ['#', 'L', 'L', '#', 'L', '#']]
        position = (4, 2)

        self.assertEqual(5, python.Day11.count_adjacent_occupied(board, position))

    def test_must_occupy_seat_return_True(self):
        board = [['L', 'L', 'L'],
                 ['L', 'L', 'L'],
                 ['L', 'L', 'L']]
        position = (1, 1)

        self.assertTrue(python.Day11.must_occupy_seat(board, position))

    def test_must_occupy_seat_return_False(self):
        board = [['L', 'L', '#'],
                 ['L', 'L', 'L'],
                 ['L', 'L', 'L']]
        position = (1, 1)

        self.assertFalse(python.Day11.must_occupy_seat(board, position))

    def test_must_free_seat_return_True(self):
        board = [['#', 'L', 'L'],
                 ['L', '#', '#'],
                 ['#', 'L', '#']]
        position = (1, 1)

        self.assertTrue(python.Day11.must_free_seat(board, position))

    def test_must_free_seat_return_False(self):
        board = [['#', 'L', 'L'],
                 ['L', '#', 'L'],
                 ['#', 'L', '#']]
        position = (1, 1)

        self.assertFalse(python.Day11.must_free_seat(board, position))

    def test_must_compute_movement(self):
        board = [['L', 'L', 'L'],
                 ['L', 'L', 'L'],
                 ['L', 'L', 'L']]
        board_expected = [['#', '#', '#'],
                          ['#', '#', '#'],
                          ['#', '#', '#']]
        self.assertEqual(board_expected, python.Day11.compute_movement(board, python.Day11.must_occupy_seat,
                                                                       python.Day11.must_free_seat))

    def test_must_compute_movement_2(self):
        board = [['#', 'L', 'L'],
                 ['L', 'L', 'L'],
                 ['L', 'L', 'L']]
        board_expected = [['#', 'L', '#'],
                          ['L', 'L', '#'],
                          ['#', '#', '#']]
        self.assertEqual(board_expected, python.Day11.compute_movement(board, python.Day11.must_occupy_seat,
                                                                       python.Day11.must_free_seat))

    def test_must_found_stable_board(self):
        with open('input_test_day11.txt') as fp:
            board = python.Day11.parse_board(fp)
        with open('input_test_day11_stable.txt') as fp:
            expected_board = python.Day11.parse_board(fp)
        self.assertEqual(expected_board, python.Day11.find_stable_state(board, python.Day11.must_occupy_seat,
                                                                        python.Day11.must_free_seat))

    def test_compute_result_must_return_37(self):
        with open('input_test_day11.txt') as fp:
            board = python.Day11.parse_board(fp)
        self.assertEqual(37, python.Day11.compute_result1(board))

    def test_count_first_seat_adjacent_must_return_8(self):
        with open('input_test_day11_2.txt') as fp:
            board = python.Day11.parse_board(fp)
            position = (3, 4)
            self.assertEqual(8, python.Day11.count_first_seat_adjacent(board, position))

    def test_compute_result2_must_return_26(self):
        with open('input_test_day11.txt') as fp:
            board = python.Day11.parse_board(fp)
        self.assertEqual(26, python.Day11.compute_result2(board))