from unittest import TestCase
from python.Day1 import Day1


class TestDay1(TestCase):
    def test_must_return_two_values(self):
        input = [1721, 979, 366, 299, 675, 1456]
        entry_list = Day1.foundTwoEntries(input)
        self.assertEqual(2, len(entry_list))

    def test_found_two_entries_that_sum_2020(self):
        input = [1721, 979, 366, 299, 675, 1456]
        entry_list = Day1.foundTwoEntries(input)

        self.assertEqual(2020, entry_list[0] + entry_list[1])

    def test_the_values_must_be_inside_input_list(self):
        input = [1721, 979, 366, 299, 675, 1456]
        entry_list = Day1.foundTwoEntries(input)

        self.assertIn(entry_list[0], input)
        self.assertIn(entry_list[1], input)

    def test_compute_result_is_514579(self):
        input = [1721, 979, 366, 299, 675, 1456]
        result = Day1.computeResult1_1(Day1.foundTwoEntries(input))
        self.assertEqual(514579, result)

    def test_must_return_three_values(self):
        input = [1721, 979, 366, 299, 675, 1456]
        entry_list = Day1.foundThreeEntries(input)
        self.assertEqual(3, len(entry_list))

    def test_compute_result_is_241861950(self):
        input = [1721, 979, 366, 299, 675, 1456]
        result = Day1.computeResult1_2(Day1.foundThreeEntries(input))
        self.assertEqual(241861950, result)


