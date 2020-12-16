from unittest import TestCase
import python.Day14


class TestDay14(TestCase):
    def test_apply_mask_to_integer_11(self):
        value = 11
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        value_expected = 73

        self.assertEqual(value_expected, python.Day14.apply_mask(value, mask))

    def test_apply_mask_to_integer_101(self):
        value = 101
        mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
        value_expected = 101

        self.assertEqual(value_expected, python.Day14.apply_mask(value, mask))

    def test_apply_address_mask(self):
        address = 42
        mask = '000000000000000000000000000000X1001X'
        expected_result = '000000000000000000000000000000X1101X'
        self.assertEqual(expected_result, python.Day14.apply_address_mask(address, mask))

    def test_demux_floating_address_mask(self):
        floating_address = '000000000000000000000000000000X1101X'
        expected_result = [26, 27, 58, 59]
        self.assertEqual(expected_result, python.Day14.demux_floating_address(floating_address))
