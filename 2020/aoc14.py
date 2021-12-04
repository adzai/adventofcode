import re

with open("aoc14-input.txt") as f:
    lines = f.readlines()

# lines = ["mask = 00110X11X0000110X0000001000111010X00"
# "mem[39993] = 276",
# "mem[23021] = 365",
# "mem[59102] = 45645",
# "mem[30606] = 2523",
# "mem[38004] = 4503",
# "mem[47790] = 1221939",
# "mem[24194] = 3417"]

res = []

def eval_binary_lst(lst):
    num = 0
    exponent = 0
    for entry in lst:
        if entry == "1":
            num += pow(2, exponent)
        exponent += 1
    return num

def solve1(lines):
    mem = dict()
    mask = []
    for line in lines:
        if line.split()[0] == "mask":
            mask = [x for x in line.split()[2]]
        else:
            instruction = list(map(int,
                                    re.findall(r"[0-9]+", line)))
            reversed_binary = list(bin(instruction[1])[2:][::-1])
            for i, char in enumerate(reversed(mask)):
                if i >= len(reversed_binary):
                    reversed_binary.append(char)
                elif char == "X":
                    pass
                else:
                    reversed_binary[i] = char
            result_decimal = eval_binary_lst(reversed_binary)
            mem[instruction[0]] = result_decimal
    return sum(mem.values())

def solve2(lines):
    mem = dict()
    for line in lines:
        if line.split()[0] == "mask":
            mask = [x for x in line.split()[2]]
        else:
            instruction = list(map(int,
                                    re.findall(r"[0-9]+", line)))
            reversed_binary = list(bin(instruction[0])[2:][::-1])
            for i, char in enumerate(reversed(mask)):
                if i >= len(reversed_binary):
                    reversed_binary.append(char)
                elif char == "X" or reversed_binary[i] == "0":
                    reversed_binary[i] = char
            res = get_mem_addresses(reversed_binary, 0, 0)
            for r in res:
                mem[r] = instruction[1]
    return sum(mem.values())

def get_mem_addresses(binary_lst, num, exponent):
    res = []
    if len(binary_lst) == 0:
        return [num]
    else:
        if binary_lst[0] == "1":
            new_num = num + pow(2, exponent)
            res += get_mem_addresses(binary_lst[1:], new_num, exponent + 1)
        elif binary_lst[0] == "X":
            new_num = num + pow(2, exponent)
            res += get_mem_addresses(binary_lst[1:], new_num, exponent + 1)
            res += get_mem_addresses(binary_lst[1:], num, exponent + 1)
        else:
            res += get_mem_addresses(binary_lst[1:], num, exponent + 1)
    return res

print(solve1(lines))
print(solve2(lines))
