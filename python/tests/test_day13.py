from unittest import TestCase
import python.Day13

class TestDay13(TestCase):
    def test_find_first_bus_from_timestamp_must_be_59_and_wait_5_minutes(self):
        bus = [7, 13, 59, 31, 19]
        earliest_bus = 939
        bus, minutes = python.Day13.find_first_bus(bus, earliest_bus)
        self.assertEqual(59, bus)
        self.assertEqual(5, minutes)