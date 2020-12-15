from unittest import TestCase
import python.Day13


class TestDay13(TestCase):
    def test_find_first_bus_from_timestamp_must_be_59_and_wait_5_minutes(self):
        bus = [7, 13, 59, 31, 19]
        earliest_bus = 939
        bus, minutes = python.Day13.find_first_bus(bus, earliest_bus)
        self.assertEqual(59, bus)
        self.assertEqual(5, minutes)

    def test_transform_bus_list_structure(self):
        bus_str = '7,13,x,x,59,x,31,19'
        bus_dict_expected = [(7,0), (13,1), (59,4), (31,6), (19, 7)]
        self.assertEqual(bus_dict_expected, python.Day13.transform_input(bus_str))

    def test_find_earliest_timestamp_must_be_1068781(self):
        bus_offsets = [(7,0), (13,1), (59,4), (31,6), (19, 7)]
        self.assertEqual(1068781, python.Day13.find_earliest_timestamp(bus_offsets))
