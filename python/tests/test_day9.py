from unittest import TestCase

import python.Day9


class TestDay9(TestCase):
    def test_True_if_number_is_result_of_two_precedent_numbers_in_preamble(self):
        preamble = 2
        numbers = [1, 2, 3]
        current_number_position = len(numbers) - 1
        self.assertTrue(python.Day9.check_validity(numbers, current_number_position, preamble))

    def test_False_if_number_is_not_result_of_two_precedent_numbers_in_preamble(self):
        preamble = 2
        numbers = [1, 2, 4]
        current_number_position = len(numbers) - 1
        self.assertFalse(python.Day9.check_validity(numbers, current_number_position, preamble))

    def test_True_if_number_is_result_of_two_precedent_numbers_in_preamble_2(self):
        preamble = 3
        numbers = [1, 2, 3, 4]
        current_number_position = len(numbers) - 1
        self.assertTrue(python.Day9.check_validity(numbers, current_number_position, preamble))

    def test_compute1_must_return_127_as_first_number_dont_follow_the_rules(self):
        preamble = 5
        with open('./input_test_day9.txt') as fp:
            self.assertEqual(127, python.Day9.compute_result_1(fp, preamble))
