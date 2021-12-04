from collections import defaultdict

def prepare_input(fname):
    lst = []
    with open(fname) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip().split()
        command = line[0]
        value = int(line[1])
        lst.append([command, value, i])
    return lst

instruction_lst = prepare_input("aoc8-input.txt")

for i in range(len(instruction_lst)):
    acc = 0
    d = defaultdict(int)
    pos = 0
    changed = False
    if instruction_lst[i][0] == "jmp":
        instruction_lst[i][0] = "nop"
        changed = True
        terminated = True
    while True:
        if pos >= len(instruction_lst):
            break
        d[tuple(instruction_lst[pos])] += 1
        if d[tuple(instruction_lst[pos])] > 1:
            terminated = False
            if changed:
                instruction_lst[i][0] = "jmp"
            break
        command = instruction_lst[pos][0]
        val = instruction_lst[pos][1]
        if command == "acc":
            acc += val
            pos += 1
        elif command == "jmp":
            pos += val
        else:
            pos += 1
    if terminated:
        break

# Both results in racket file
print("Part2:", acc)
