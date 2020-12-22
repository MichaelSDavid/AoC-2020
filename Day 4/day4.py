from re import match

# Part 1
with open("input.txt") as f:
    data = [data.split() for data in f.read().split("\n\n")]
    
    p_data = []
    for d in data:
        p_pairs = {}
        for key_value in d:
            key_value = key_value.split(":")
            key = key_value[0]
            value = key_value[1]

            p_pairs[key] = value
        p_data.append(p_pairs)

fields = {
            "byr": lambda y: match("\d{4}",y) and 1920 <= int(y) <= 2002,
            "iyr": lambda y: match("\d{4}",y) and 2010 <= int(y) <= 2020,
            "eyr": lambda y: match("\d{4}",y) and 2020 <= int(y) <= 2030,
            "hgt": lambda h: match("\d+(cm|in)",h) and \
            ((h[-2:] == "cm" and 150 <= int(h[:-2]) <= 193) or \
             (h[-2:] == "in" and 59 <= int(h[:-2]) <= 76)),
            "hcl": lambda c: match("#[0-9a-f]{6}",c),
            "ecl": lambda c: match("amb|blu|brn|gry|grn|hzl|oth",c),
            "pid": lambda i: match("^\d{9}$",i)
         }

valid_n1 = 0
valid_n2 = 0
for d in p_data:
    v1 = True
    v2 = True
    for field in fields:
        check = fields[field]
        if field not in d:
            v1 = False
        elif not check(d[field]):
            v2 = False
    
    if v1:
        valid_n1 += 1
        if v2:
            valid_n2 += 1

print(f"Num Valid (1): {valid_n1}\n")

# Part 2
print(f"Num Valid (2): {valid_n2}")
