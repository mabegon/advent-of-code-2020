from unittest import TestCase
import python.Day4


class TestDay3(TestCase):
    def test_must_validate_passport_example_1(self):
        passport = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
                    'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
                    'cid': '147', 'hgt': '183cm'}
        self.assertTrue(python.Day4.validatePassport(passport))

    def test_must_invalidate_passport_example_2(self):
        passport = {'iyr': '2013', 'ecl': 'amb', 'cid': '350',
                    'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d',
                    'byr': '1929'}
        self.assertFalse(python.Day4.validatePassport(passport))

    def test_must_validate_passport_example_3(self):
        passport = {'hcl': '#ae17e1', 'iyr': '2013',
                    'eyr': '2024', 'ecl': 'brn',
                    'pid': '760753108', 'byr': '1931',
                    'hgt': '179cm'}
        self.assertTrue(python.Day4.validatePassport(passport))

    def test_must_invalidate_passport_example_4(self):
        passport = {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648',
                    'iyr': '2011', 'ecl': 'brn', 'hgt': '59in', }
        self.assertFalse(python.Day4.validatePassport(passport))

    def test_must_parse_a_passport(self):
        passport_1 = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
                    'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
                    'cid': '147', 'hgt': '183cm'}

        expected_passports = [passport_1]

        with open('./input_test_day4_simple.txt') as fp:
            passports = python.Day4.parse_passports(fp)
            self.assertEqual(expected_passports,passports)

    def test_must_parse_input_passports(self):
        passport_1 = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
                    'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
                    'cid': '147', 'hgt': '183cm'}
        passport_2 = {'iyr': '2013', 'ecl': 'amb', 'cid': '350',
                    'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d',
                    'byr': '1929'}
        passport_3 = {'hcl': '#ae17e1', 'iyr': '2013',
                    'eyr': '2024', 'ecl': 'brn',
                    'pid': '760753108', 'byr': '1931',
                    'hgt': '179cm'}
        passport_4 = {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648',
                    'iyr': '2011', 'ecl': 'brn', 'hgt': '59in', }

        expected_passports = [passport_1,passport_2, passport_3, passport_4]

        with open('./input_test_day4.txt') as fp:
            passports = python.Day4.parse_passports(fp)
            self.assertEqual(expected_passports,passports)
