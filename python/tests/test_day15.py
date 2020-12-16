from unittest import TestCase

import python.Day15


class TestDay15(TestCase):
    def test_compute_result1_must_be_436(self):
        input = [0, 3, 6]
        result_expected = 436
        turns = 2020
        self.assertEqual(result_expected, python.Day15.compute_result1(input, turns))

    def test_compute_result1_must_be_175594(self):
        input = [0, 3, 6]
        result_expected = 175594
        turns = 30000000
        self.assertEqual(result_expected, python.Day15.compute_result1(input, turns))