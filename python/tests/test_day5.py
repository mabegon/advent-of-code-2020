from unittest import TestCase
import python.Day5


class TestDay5(TestCase):
    def test_must_select_low_patition(self):
        expected_min = 0
        expected_max = 63

        min, max = python.Day5.select_partition(0, 127, 'F')
        self.assertEqual(expected_min, min)
        self.assertEqual(expected_max, max)

    def test_must_select_high_patition(self):
        expected_min = 32
        expected_max = 63

        min, max = python.Day5.select_partition(0, 63, 'B')
        self.assertEqual(expected_min, min)
        self.assertEqual(expected_max, max)

    def test_must_select_low_patition_2(self):
        expected_min = 32
        expected_max = 47

        min, max = python.Day5.select_partition(32, 63, 'F')
        self.assertEqual(expected_min, min)
        self.assertEqual(expected_max, max)

    def test_must_select_row_44(self):
        self.assertEqual(44, python.Day5.select_row('FBFBBFF'))

    def test_input_RLR_must_select_column_5(self):
        self.assertEqual(5, python.Day5.select_column('RLR'))

    def test_input_FBFBBFFRLR_must_select_seat_357(self):
        self.assertEqual(357, python.Day5.select_seat('FBFBBFFRLR'))
