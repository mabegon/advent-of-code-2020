import re


def validate_byr(byr_value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    try:
        return int(byr_value) >= 1920 and int(byr_value) <= 2002
    except:
        return False


def validate_iyr(iyr_value):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    try:
        return int(iyr_value) >= 2010 and int(iyr_value) <= 2020
    except:
        return False


def validate_eyr(eyr_value):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    try:
        return int(eyr_value) >= 2020 and int(eyr_value) <= 2030
    except:
        return False


def validate_hgt(hgt_value):
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    m = re.match('(?P<number>\d+)(?P<unit>cm|in)', hgt_value.lower())
    if m is None:
        return False
    value = m.groupdict()
    if value['unit'] == 'cm':
        return int(value['number']) >= 150 and int(value['number']) <= 193
    else:
        return int(value['number']) >= 59 and int(value['number']) <= 76


def validate_hcl(hcl_value):
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    m = re.match('^#(\d|[a-f]){6}$', hcl_value.lower())
    if m is None:
        return False
    else:
        return True


# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def validate_ecl(ecl_value):
    accepted_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return len(ecl_value) == 3 and ecl_value in accepted_values


# pid (Passport ID) - a nine-digit number, including leading zeroes.
def validate_pid(pid_value):
    m = re.match('^(\d){9}$', pid_value)
    if m is None:
        return False
    else:
        return True


def validate_cid(cid_value):
    # cid (Country ID) - ignored, missing or not.
    return True


required_fields = {'byr': validate_byr,
                   'iyr': validate_iyr,
                   'eyr': validate_eyr,
                   'hgt': validate_hgt,
                   'hcl': validate_hcl,
                   'ecl': validate_ecl,
                   'pid': validate_pid,
                   'cid': validate_cid}


def is_correct_passport(passport):
    missing_fields = [field for field in required_fields if field not in passport.keys()]
    return len(missing_fields) == 0 or missing_fields == ['cid']


def validate_fields(passport):
    validated = True;
    for field in passport.keys():
        validated = validated and required_fields[field](passport[field])
    return validated


def validate_passport(passport):
    return is_correct_passport(passport) and validate_fields(passport)


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
    correct_passports = 0
    valid_passports = 0

    with open('../input_day4_1.txt') as input_fp:
        passports = parse_passports(input_fp)
        for passport in passports:
            if is_correct_passport(passport):
                correct_passports += 1
        for passport in passports:
            if validate_passport(passport):
                valid_passports += 1
    print(f'Nb of correct passports is {correct_passports}/{len(passports)}')
    print(f'Nb of valid passports is {valid_passports}/{len(passports)}')


if __name__ == '__main__':
    main()
