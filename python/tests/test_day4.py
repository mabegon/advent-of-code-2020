from unittest import TestCase
import python.Day4


class TestDay4(TestCase):
    def test_must_validate_passport_example_1(self):
        passport = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
                    'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
                    'cid': '147', 'hgt': '183cm'}
        self.assertTrue(python.Day4.is_correct_passport(passport))

    def test_must_invalidate_passport_example_2(self):
        passport = {'iyr': '2013', 'ecl': 'amb', 'cid': '350',
                    'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d',
                    'byr': '1929'}
        self.assertFalse(python.Day4.is_correct_passport(passport))

    def test_must_validate_passport_example_3(self):
        passport = {'hcl': '#ae17e1', 'iyr': '2013',
                    'eyr': '2024', 'ecl': 'brn',
                    'pid': '760753108', 'byr': '1931',
                    'hgt': '179cm'}
        self.assertTrue(python.Day4.is_correct_passport(passport))

    def test_must_invalidate_passport_example_4(self):
        passport = {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648',
                    'iyr': '2011', 'ecl': 'brn', 'hgt': '59in', }
        self.assertFalse(python.Day4.is_correct_passport(passport))

    def test_must_parse_a_passport(self):
        passport_1 = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020',
                      'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
                      'cid': '147', 'hgt': '183cm'}

        expected_passports = [passport_1]

        with open('./input_test_day4_simple.txt') as fp:
            passports = python.Day4.parse_passports(fp)
            self.assertEqual(expected_passports, passports)

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

        expected_passports = [passport_1, passport_2, passport_3, passport_4]

        with open('./input_test_day4.txt') as fp:
            passports = python.Day4.parse_passports(fp)
            self.assertEqual(expected_passports, passports)

    def test_1920_must_be_a_valid_bry(self):
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        self.assertTrue(python.Day4.validate_byr('1920'))

    def test_2002_must_be_a_valid_bry(self):
        self.assertTrue(python.Day4.validate_byr('2002'))

    def test_1919_must_be_a_invalid_bry(self):
        self.assertFalse(python.Day4.validate_byr('1919'))

    def test_abcd_must_be_a_invalid_bry(self):
        self.assertFalse(python.Day4.validate_byr('abcd'))

    def test_150cm_must_be_a_valid_hgt(self):
        self.assertTrue(python.Day4.validate_hgt('150cm'))

    def test_150CM_must_be_a_valid_hgt(self):
        self.assertTrue(python.Day4.validate_hgt('150CM'))

    def test_59in_must_be_a_valid_hgt(self):
        self.assertTrue(python.Day4.validate_hgt('59in'))

    def test_150in_must_be_a_invalid_hgt(self):
        self.assertFalse(python.Day4.validate_hgt('150in'))

    def test_150f4in_must_be_a_invalid_hgt(self):
        self.assertFalse(python.Day4.validate_hgt('150f4in'))

    def test_sharp_ae17e1_must_be_a_valid_hcl(self):
        self.assertTrue(python.Day4.validate_hcl('#ae17e1'))

    def test_blu_must_be_a_valid_ecl(self):
        self.assertTrue(python.Day4.validate_ecl('blu'))

    def test_blue_must_be_a_invalid_ecl(self):
        self.assertFalse(python.Day4.validate_ecl('blue'))

    def test_000000000_must_be_a_valid_pid(self):
        self.assertTrue(python.Day4.validate_pid('000000000'))

    def test_23_must_be_a_invalid_pid(self):
        self.assertFalse(python.Day4.validate_pid('23'))

    def test_must_be_a_valid_passport(self):
        passport = {'iyr': '2010','hgt': '158cm','hcl': '#b6652a',
                    'ecl': 'blu', 'byr': '1944', 'eyr': '2021', 'pid': '093154719'}
        self.assertTrue(python.Day4.validate_passport(passport))

    def test_must_be_a_invalid_passport(self):

        passport = {'iyr': '2012','hgt': '182cm','hcl': 'dab227', 'cid':'277',
                    'ecl': 'brn', 'byr': '1992', 'eyr': '2020', 'pid': '021572410'}
        self.assertFalse(python.Day4.validate_passport(passport))