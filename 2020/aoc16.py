import re

with open("aoc16-input.txt") as f:
    lines = f.readlines()

ranges_parse = True
ctr = 0
nums = []
d = dict()
for line in lines:
    if line == "\n":
        if ctr == 0:
            ranges_parse = False
            is_my_ticket = True
            ctr += 1
        elif ctr == 1:
            is_my_ticket = False
            ctr += 1
        continue
    elif ranges_parse:
        name = line.split(":")[0]
        r = list(map(int, re.findall(r"[0-9]+(?!-)[0-9]+", line)))
        d[name] = (range(r[0], r[1] +1), range(r[2], r[3] + 1))
    elif is_my_ticket:
        if "your ticket:" in line:
            continue
        my_ticket = list(map(int, line.split(",")))
    else:
        if "nearby tickets:" in line:
            continue
        nums.append(list(map(int, line.split(","))))

# lines = ["class: 1-3 or 5-7",
# "row: 6-11 or 33-44",
# "seat: 13-40 or 45-50"]
# d = {"class": (range(0, 2), range(4, 20)), "row": (range(0, 6), range(8, 20)), "seat": (range(0, 14), range(16, 20))}
# my_ticket = [11, 12, 13]
# nums = [[3, 9, 18],
# [15, 1, 5],
# [5, 14, 9]]
invalid_nums = []
valid_tickets = []
def solve1():
    for row in nums:
        valid_row = True
        valid_nums = []
        for num in row:
            num_arr = []
            valid = False
            for key, r in d.items():
                if num in r[0] or num in r[1]:
                    valid = True
                    num_arr.append(key)
            if not valid:
                invalid_nums.append(num)
                valid_row = False
            else:
                valid_nums.append(num_arr)
        if valid_row:
            valid_tickets.append(valid_nums)
    return valid_tickets, invalid_nums

valid_tickets, invalid_nums = solve1()
print("Part1:", sum(invalid_nums))

def return_shared(l1, l2):
    lst = []
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    else:
        for item in l2:
            if item in l1:
                lst.append(item)
        return lst



def solve2():
    i = 0
    possibilites = []
    while i < len(valid_tickets[0]):
        current_result = []
        for row in valid_tickets:
            current_result = return_shared(current_result, row[i])
        possibilites.append(current_result)
        i += 1
    return possibilites

result = solve2()
length = 1
result_dict = dict()
while length < len(result):
    for i, values in enumerate(result):
        if len(values) == length:
            for val in values:
                if val not in result_dict.values():
                    result_dict[i] = val
    length += 1
result_nums = []
for k, v in result_dict.items():
    if "departure" in v:
        result_nums.append(my_ticket[k])
num = result_nums[0]
for n in result_nums[1:]:
    num *= n

print("Part2:", num)
