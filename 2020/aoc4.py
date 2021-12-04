import re

with open("aoc4-input.txt") as f:
    lines = f.read().split("\n\n")

valid_num = 0
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
num = 0

for line in lines:
    line = line.replace("\n", " ")
    vals = line.split()
    num = 0
    for val in vals:
        spl = val.split(":")
        key = spl[0]
        val = spl[1]
        if key in required:
            print(key)
            print(val)
            if key == "hcl":
                x = re.match(r"#([a-f]|[0-9]){6}", val)
                if x is not None:
                    num += 1
            elif key == "byr":
                if int(val) in range(1920, 2002 + 1):
                    num += 1
            elif key == "iyr":
                if int(val) in range(2010, 2020 + 1):
                    num += 1
            elif key == "eyr":
                if int(val) in range(2020, 2030 + 1):
                    num += 1
            elif key == "hgt":
                if val.endswith("cm"):
                    if int(val.replace("cm", "")) in range(150, 193 + 1):
                        num += 1
                elif val.endswith("in"):
                    if int(val.replace("in", "")) in range(59, 76 + 1):
                        num += 1
            elif key == "ecl":
                if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    num += 1
            elif key == "pid":
                if len(val) == 9:
                    num += 1
    if num == 7:
        valid_num += 1
print(valid_num)
