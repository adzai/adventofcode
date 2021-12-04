def prepare_input(fname):
    with open(fname) as f:
        return list(map(int, f.readlines()))

def find(lines):
    ptr = 25
    for i in range(len(lines)):
        preamble = lines[i:ptr]
        num = lines[ptr]
        found = False
        for j in range(len(preamble)):
            for k in range(j+1, len(preamble)):
                if preamble[j] + preamble[k] == num:
                    found = True
        if found:
            ptr += 1
        else:
            break
    return num

def find_range(lines, target_num):
    nums = [lines[0]]
    for num in lines[1:]:
        nums.append(num)
        if sum(nums) == target_num:
            return min(nums) + max(nums)
        while sum(nums) > target_num:
            nums.pop(0)

lines = prepare_input("aoc9-input.txt")
res1 = find(lines)
print("Part 1:", res1)
res2 = find_range(lines, res1)
print("Part 2:", res2)
