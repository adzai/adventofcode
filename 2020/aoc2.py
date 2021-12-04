import re

reg_exp = "([0-9]+-[0-9]+)\\s([a-z])\\W+(\\w+)"
with open("aoc2-input.txt") as f:
    text = f.read()
vectors = re.findall(reg_exp, text)
valid_passwords = 0

# First part
for entry in vectors:
    password = entry[2]
    char_to_find = entry[1]
    nums = re.findall("([0-9]+)-([0-9]+)", entry[0])[0]
    num_range = range(int(nums[0]), int(nums[1]) + 1)
    d = {char_to_find: 0}
    for char in password:
        if char == char_to_find:
            d[char] += 1
    if d[char_to_find] in num_range:
        valid_passwords += 1

print(valid_passwords)
valid_passwords = 0

# Second part
for entry in vectors:
    password = entry[2]
    char_to_find = entry[1]
    nums = re.findall("([0-9]+)-([0-9]+)", entry[0])[0]
    if (password[int(nums[0]) - 1] == char_to_find) ^ \
            (password[int(nums[1]) - 1] == char_to_find):
        valid_passwords += 1

print(valid_passwords)
