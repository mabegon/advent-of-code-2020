from unittest import TestCase
import python.Day16

class TestDay16(TestCase):
    def test_add_rule(self):
        rule_line = 'class: 1-3 or 5-7'
        rules = {}
        rules_expected = {1:['class'],
                          2:['class'],
                          3:['class'],
                          5:['class'],
                          6:['class'],
                          7:['class']}
        self.assertEqual(rules_expected, python.Day16.add_rule(rules, rule_line))

    def test_compute_result1(self):
        with open('input_test_day16.txt') as fp:
            self.assertEqual(71, python.Day16.compute_result1(fp))