import re


def validatePassport(passport):
    required_fields = ['byr',
                       'iyr',
                       'eyr',
                       'hgt',
                       'hcl',
                       'ecl',
                       'pid',
                       'cid']

    missing_fields = [field for field in required_fields if field not in passport.keys()]
    return len(missing_fields) == 0 or missing_fields == ['cid']


def parse_passports(fp):
    passports = []
    current_passport = {}
    for line in fp:
        if line.strip() == '':
            passports.append(current_passport)
            current_passport = {}
        else:
            fields = re.findall('(?P<field>...):(?P<value>\S+)', line.strip())
            for field in fields:
                current_passport[field[0]] = field[1]

    if current_passport != {}:
        passports.append(current_passport)

    return passports


def main():
    valid_passports = 0
    with open('../input_day4_1.txt') as input_fp:
        passports = parse_passports(input_fp)
        for passport in passports:
            if (validatePassport(passport)):
                valid_passports += 1

    print(f'Nb of valid passports is {valid_passports}/{len(passports)}')


if __name__ == '__main__':
    main()
