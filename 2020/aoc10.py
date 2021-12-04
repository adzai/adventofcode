from functools import lru_cache

with open("aoc10-input.txt") as f:
    lines = f.readlines()
lines = list(map(int, lines))
# lines = [
#     16,
#     10,
#     15,
#     5,
#     1,
#     11, 7,
#     19,
#     6,
#     12,
#     4
# ]
ctr1, ctr2 = 0, 0
lines = sorted(lines)
lines = [0] + lines
lines.append(lines[-1] + 3)
for i in range(len(lines) - 1):
    if lines[i] + 1 == lines[i+1]:
        ctr1 += 1
    elif lines[i] + 3 == lines[i+1]:
        ctr2 += 1

print(ctr1 * ctr2)

# TODO: Stop cheating and optimize manually


@lru_cache(maxsize=128)
def recur(lines, ptr):
    x = 0
    if ptr + 1 >= len(lines) - 1:
        return 1
    i = ptr+1
    while lines[i] - lines[ptr] <= 3:
        x += recur(lines, i)
        i += 1
    return x


print(recur(tuple(lines), 0))
print(recur.cache_info())

paths = {lines[0]: 1}
print(lines)
# print("X: 0 Paths: 1")
for x in lines[1:]:
    paths[x] = sum(paths[x-y] for y in range(1, 4) if x-y in paths)
    # print("X:", x, end=" ")
    # print("Paths:", paths[x])
print('Part 2: {}'.format(paths[lines[-1]]))
