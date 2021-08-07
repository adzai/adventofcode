from collections import defaultdict
from itertools import permutations

with open("13.txt") as f:
    lines = f.readlines()


def get_happiness(v1, v2):
    h = hash("".join(sorted(v1 + v2)))
    return cost_hash[h]


def get_final_happiness(people_perms):
    final_happiness = 0
    for people in people_perms:
        happiness = 0
        for i in range(len(people) - 1):
            v1 = people[i]
            v2 = people[i + 1]
            happiness += get_happiness(v1, v2)
        happiness += get_happiness(people[0], people[-1])
        final_happiness = max(happiness, final_happiness)
    return final_happiness


def get_cost_between_edges(lines):
    d = defaultdict(int)
    for line in lines:
        split = line.split()
        multiplier = -1 if split[2] == "lose" else 1
        v1 = split[0]
        v2 = split[-1].replace(".", "")
        cost = multiplier * int(split[3])
        h = hash("".join(sorted(v1 + v2)))
        d[h] += cost
    return d


cost_hash = get_cost_between_edges(lines)
people = list(set([line.split()[0] for line in lines]))
people_perms_p1 = list(permutations(people))
people_perms_p2 = list(permutations(people + ["me"]))

print("Part 1: ", get_final_happiness(people_perms_p1))
print("Part 2: ", get_final_happiness(people_perms_p2))
