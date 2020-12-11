from unittest import TestCase

import python.Day10


class TestDay10(TestCase):
    def test_must_return_device_joltage(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]
        self.assertEqual(22, python.Day10.device_joltage(adapters))

    def test_must_return_best_fit_device_by_rating_0(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        rating=0
        self.assertEqual(1, python.Day10.select_best_adapter(adapters, rating))

    def test_must_return_best_fit_device_by_rating_1(self):
        adapters = [16, 10, 15, 5, 11, 7, 19, 6, 12, 4]
        rating=1
        self.assertEqual(4, python.Day10.select_best_adapter(adapters, rating))

    def test_must_return_best_fit_device_by_rating_4(self):
        adapters = [16, 10, 15, 5, 11, 7, 19, 6, 12]
        rating=4
        self.assertEqual(5, python.Day10.select_best_adapter(adapters, rating))

    def test_must_return_best_fit_device_by_rating_4(self):
        adapters = [16, 10, 15, 5, 11, 7, 19, 6, 12]
        rating=4
        self.assertEqual(5, python.Day10.select_best_adapter(adapters, rating))

    def test_compute_result1_must_return_35(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.assertEqual(35, python.Day10.compute_result1(adapters))

    def test_compute_result1_must_return_220(self):
        with open('input_test_day10.txt') as fp:
            adapters = python.Day10.parse_input(fp)
        self.assertEqual(220, python.Day10.compute_result1(adapters))

    def test_compute_result2_must_return_8(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.assertEqual(8, python.Day10.compute_result2(adapters))

    def test_compute_result1_must_return_19208(self):
        with open('input_test_day10.txt') as fp:
            adapters = python.Day10.parse_input(fp)
        self.assertEqual(19208, python.Day10.compute_result2(adapters))