from unittest import TestCase
from python.Day2 import Day2


class TestDay2(TestCase):
    def test_regexp_found_all_values(self):
        line = "2-8 d: pddzddkdvqgxndd"
        dict = Day2.parseLine(line)
        self.assertEqual(2, dict['number1'])
        self.assertEqual(8, dict['number2'])
        self.assertEqual('d', dict['letter'])
        self.assertEqual('pddzddkdvqgxndd', dict['password'])

    def test_validate_with_policy_rules_one_must_be_True(self):
        min, max, letter, password = 1,3, 'a', 'abcde'
        self.assertTrue(Day2.validatePasswordWithPolicyRules1(min, max, letter, password))

    def test_validate_with_policy_rules_one_must_be_False(self):
        min, max, letter, password = 1, 3, 'b', 'cdefg'
        self.assertFalse(Day2.validatePasswordWithPolicyRules1(min, max, letter, password))

    def test_validate_with_policy_rules_Two_must_be_True(self):
        min, max, letter, password = 1,3, 'a', 'abcde'
        self.assertTrue(Day2.validatePasswordWithPolicyRules2(min, max, letter, password))

    def test_validate_with_policy_rules_Two_must_be_False(self):
        min, max, letter, password = 1, 3, 'b', 'cdefg'
        self.assertFalse(Day2.validatePasswordWithPolicyRules2(min, max, letter, password))

    def test_validate_with_policy_rules_Two_must_be_False_2(self):
        min, max, letter, password = 2, 9, 'c', 'ccccccccc'
        self.assertFalse(Day2.validatePasswordWithPolicyRules2(min, max, letter, password))