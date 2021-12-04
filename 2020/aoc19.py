import re

with open("aoc19-input.txt") as f:
    lines = f.readlines()

def apply_rule(key, depth):
    if depth > 15:
        return ""
    if key.isnumeric():
        rule = d[key]
        chars = ""
        for r in rule[0]:
            chars += apply_rule(r, depth+1)
        if len(rule) > 1:
            c = ""
            for r in rule[1]:
                c += apply_rule(r, depth+1)
            return '(' + chars + "|" + c + ")"
        else:
            return chars
    else:
        return key.strip('"')

parse_rules = True
statements = []
d = dict()
for line in lines:
    if line == "\n":
        parse_rules = False
    elif parse_rules:
        line = line.strip().split(":")
        rule_number = line[0]
        rules = [x.strip().split() for x in line[1].split("|")]
        d[rule_number] = rules
    else:
        statements.append(line)

regex1 = "^" + apply_rule('0', 0) + "$"
res_arr = []
for stmt in statements:
    if re.match(regex1, stmt):
        res_arr.append(stmt)

print("Part 1:", len(res_arr))

d['8'] = [['42'], ['42', '8']]
d['11'] = [['42', '31'], ['42', '11', '31']]
regex2 = "^" + apply_rule('0', 0) + "$"
res_arr = []
for stmt in statements:
    if re.match(regex2, stmt):
        res_arr.append(stmt)

print("Part 2:", len(res_arr))
