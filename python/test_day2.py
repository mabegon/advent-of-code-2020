from unittest import TestCase
from day2 import Day2


class TestDay2(TestCase):
    def test_regexp_found_all_values(self):
        line = "2-8 d: pddzddkdvqgxndd"
        dict = Day2.parseLine(line)
        self.assertEqual(2, dict['min'])
        self.assertEqual(8, dict['max'])
        self.assertEqual('d', dict['letter'])
        self.assertEqual('pddzddkdvqgxndd', dict['password'])

    def test_validate_must_be_True(self):
        min, max, letter, password = 1,3, 'a', 'abcde'
        self.assertTrue(Day2.validatePassword(min, max, letter, password))

    def test_validate_must_be_False(self):
        min, max, letter, password = 1, 3, 'b', 'cdefg'
        self.assertFalse(Day2.validatePassword(min, max, letter, password))


