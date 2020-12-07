from unittest import TestCase
import python.Day7


class Test_Day7(TestCase):
    def test_must_parse_3_bags_in_line(self):
        line = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
        result_expected = ('light red', {'bright white': 1, 'muted yellow': 2})
        self.assertEqual(result_expected, python.Day7.parse_line(line))

    def test_must_return_who_can_hold_directly_by_rule(self):
        container_bag = 'light red'
        contents_bag = {'bright white': 1, 'muted yellow': 2}
        result_expected = {'bright white': 'light red',
                           'muted yellow': 'light red',
                           }
        self.assertEqual(result_expected, python.Day7.who_can_hold_by_rule(container_bag, contents_bag))

    def test_must_return_who_can_hold_directly_by_rules(self):
        rules = {}
        rules['light red'] = {'bright white': 1, 'muted yellow': 2}
        rules['dark orange'] = {'bright white': 1, 'muted yellow': 2}
        rules['bright white'] = {'shiny gold': 1}

        result_expected = {'bright white': ['light red', 'dark orange'],
                           'muted yellow': ['light red', 'dark orange'],
                           'shiny gold': ['bright white']}
        self.assertEqual(result_expected, python.Day7.who_can_hold_by_rules(rules))


    def test_must_return_4_for_shiny_gold_input(self):
        with open('./input_test_day7.txt') as rules_file:
            rules = python.Day7.get_rules(rules_file) #Must be tested
            self.assertEqual(4, python.Day7.compute_question_1(rules, 'shiny gold'))

    def test_must_return_32(self):
        rules = {}
        rules['faded blue'] = None
        rules['dotted black'] = None
        rules['vibrant plum'] = {'faded blue': 5, 'dotted black': 6 }
        rules['dark olive'] = {'faded blue': 3, 'dotted black': 4 }
        rules['shiny gold'] = {'dark olive': 1, 'vibrant plum': 2}
        self.assertEqual(32, python.Day7.compute_question_2(rules, 'shiny gold'))
