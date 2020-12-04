import re

passports = [dict(v.split(':') for v in l) for l in [s.strip().replace(' ', '\n').split('\n') for s in open('../input.txt').read().split('\n\n')]]

hcl = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')
pid = re.compile(r'^(\d{9})$')

def has_all_fields(passport):
    return all(field in passport for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def has_valid_fields(passport):
    if not has_all_fields(passport): return False

    if not 1920 <= int(passport['byr']) <= 2002: return False
    if not 2010 <= int(passport['iyr']) <= 2020: return False
    if not 2020 <= int(passport['eyr']) <= 2030: return False

    if passport['hgt'][-2:] == 'cm':
        if not 150 <= int(passport['hgt'][:-2]) <= 193: return False
    elif passport['hgt'][-2:] == 'in':
        if not 59 <= int(passport['hgt'][:-2]) <= 76: return False
    else: return False

    if not hcl.match(passport['hcl']): return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False

    if not pid.match(passport['pid']): return False

    return True

print(sum(has_all_fields(passport) for passport in passports))
print(sum(has_valid_fields(passport) for passport in passports))
