with open("aoc10-input.txt") as f:
    lines = f.readlines()

lines = sorted(list(map(int, lines)))

# test input
# lines = sorted([16,
#                 10,
#                 15,
#                 5,
#                 1,
#                 11,
#                 7,
#                 19,
#                 6,
#                 12,
#                 4])

# add first and last adapter
nums = [0] + lines + [lines[-1] + 3]
d = {1:0, 3:0}

for i in range(len(nums) - 1):
    d[nums[i+1] - nums[i]] += 1
print("Part1:", d[1] * d[3])

paths_dict = dict()
paths_dict[0] = 1
for num in nums[1:]:
    x = num - 1
    sum_of_paths = 0
    while num - x <= 3:
        if (walrus := paths_dict.get(x)):
            sum_of_paths += walrus
        x -= 1
    paths_dict[num] = sum_of_paths
print("Part2:", paths_dict[nums[-1]])
