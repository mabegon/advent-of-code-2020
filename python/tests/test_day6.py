from unittest import TestCase
import python.Day6


class TestDay6(TestCase):
    def test_must_be_found_5_groups(self):
        with open('./input_test_day6.txt') as fp:
            self.assertEqual(5, len(python.Day6.count_yes_groups(fp)))

    def test_result_must_be_11(self):
        with open('./input_test_day6.txt') as fp:
            self.assertEqual(11, python.Day6.compute_result(fp))
