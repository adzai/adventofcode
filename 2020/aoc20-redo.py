import numpy as np
import re

with open("test.txt") as f:
# with open("aoc20-input.txt") as f:
    lines = f.readlines()

h_map = dict()
count_dict = dict()
for line in lines:
    if line == "\n":
        continue
    elif "Tile" in line:
        current_tile = int(re.findall("[0-9]+", line)[0])
        h_map[current_tile] = []
    else:
        h_map[current_tile].append(list(line.strip("\n")))
        count_dict[current_tile] = dict()

# print(h_map)

def get_edges(arr):
    le = [x[0] for x in arr]
    re = [x[-1] for x in arr]
    te = arr[0]
    be = arr[-1]
    d = dict()
    d[0] = re
    d[1] = te
    d[2] = le
    d[3] = be
    return d

# N = len(h_map[2953])
N = len(h_map[1951])

# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
def rotate_matrix(mat):

    # Consider all squares one by one
    for x in range(0, int(N / 2)):

        # Consider elements in group
        # of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = mat[x][y]

            # move values from right to top
            mat[x][y] = mat[y][N-1-x]

            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]

            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]

            # assign temp to left
            mat[N-1-y][x] = temp

def flip(key):
    for i in range(len(h_map[key])):
        h_map[key][i] = h_map[key][i][::-1]

def check_fit(chosen):
    curr_edges = get_edges(h_map[chosen])
    print(chosen)
    print(curr_edges)
    for key, vals in h_map.items():
        if key == chosen:
            continue
        ctr = 0
        while ctr < 2:
            added = False
            edges = get_edges(vals)
            for k1 in range(4):
                e1 = edges[k1]
                for k2, e2 in curr_edges.items():
                    # if key not in count_dict[chosen].values():
                    if e1 == e2:
                        dest = (k2 + 2) % 4
                        shift = (dest - k1) % 4
                        # print("k", k1, k2)
                        # print("dest", dest)
                        print(shift)
                        for i in range(shift):
                            print("DDD", h_map[key][0])
                            rotate_matrix(h_map[key])
                            print(h_map[key][0])
                        count_dict[chosen][key]  = k2
                        added = True

            if ctr == 1 and not added:
                flip(key)
            if added:
                print(added)
                print(key)
                ctr += 2
            else:
                print("Flip")
                flip(key)
                ctr += 1

for keyword in h_map.keys():
    check_fit(keyword)

print(count_dict)
for x in h_map.keys():
    print(x)
    for y in h_map[x]:
        print("".join(y))

