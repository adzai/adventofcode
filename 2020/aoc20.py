from collections import defaultdict
import re

with open("test.txt") as f:
# with open("aoc20-input.txt") as f:
    lines = f.readlines()

h_map = dict()
for line in lines:
    if line == "\n":
        continue
    elif "Tile" in line:
        current_tile = int(re.findall("[0-9]+", line)[0])
        h_map[current_tile] = []
    else:
        h_map[current_tile].append(line.strip("\n"))

def get_edges(arr):
    le = "".join([x[0] for x in arr])
    re = "".join([x[-1] for x in arr])
    te = arr[0]
    be = arr[-1]
    d = dict()
    d[0] = re
    d[1] = te
    d[2] = le
    d[3] = be
    return d

count_dict = dict()
hash_map = dict()
for k, v in h_map.items():
    e = get_edges(v)
    hash_map[k] = e
    count_dict[k] = dict()


cache = []
def rotate_map(key, shift, flipped):
    global cache
    nd = dict()
    for x in count_dict[key].keys():
        if x not in cache:
            cache.append(x)
            rotate_map(x, shift, flipped)
        num = (count_dict[key][x] + shift) % 4
        if flipped == 1:
            if num == 2:
                num = 0
            elif num == 0:
                num = 2
            nd[x] = num
        else:
            nd[x] = num
    count_dict[key] = nd



def rotate(key, dest, curr, flipped, chosen):
    global cache
    arr_map = hash_map[key]
    shift = (dest - curr) % 4
    new_dict = dict()
    for i in range(4):
        new_dict[i] = arr_map[(i+shift)%4]
    hash_map[key] = new_dict
    cache.append(key)
    cache.append(chosen)
    rotate_map(key, shift, flipped)
    cache = []


def check_fit(chosen):
    curr_edges = hash_map[chosen]
    for key, vals in hash_map.items():
        if key == chosen:
            continue
        edges = vals
        ctr = 0
        added = True
        while ctr < 2:
            added = False
            for k1 in range(4):
                e1 = edges[k1]
                for k2, e2 in curr_edges.items():
                    if key not in count_dict[chosen].values():
                        if e1 == e2:
                            dest = (k2 + 2) % 4
                            rotate(key, dest, k1, ctr, chosen)
                            count_dict[chosen][key]  = k2
                            added = True
            #flip code
            if added:
                # tmp = edges[0][::-1]
                # edges[0] = tmp
                # edges[1] = edges[1][::-1]
                # edges[2] = edges[2][::-1]
                # edges[3] = edges[3][::-1]
                ctr += 2
            else:
                edges[0] = edges[0][::-1]
                edges[1] = edges[1][::-1]
                edges[2] = edges[2][::-1]
                edges[3] = edges[3][::-1]
                ctr += 1

for keyword in hash_map.keys():
    try:
        print(count_dict[1951])
    except:
        pass
    check_fit(keyword)

sums = []
for x, y in count_dict.items():
    if len(y) < 3:
        sums.append(x)

s = sums[0]
print(sums)
for x in sums[1:]:
    s *= x

start = count_dict[sums[1]]


# 03
# 23
# 01 #
# 21 #
print(start)
print("Part1", s)



print(count_dict)
# for x in h_map.keys():
#     print(x)
#     for y in h_map[x]:
#         print("".join(y))
