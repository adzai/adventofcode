from collections import defaultdict

# with open("exp21.txt") as f:
with open("aoc21-input.txt") as f:
    lines = f.readlines()

d = dict()
found_foods = defaultdict(int)
for line in lines:
    foods, allergens = line.replace(")\n", "").split(" (contains ")
    foods = foods.split()
    for food in foods:
        found_foods[food] += 1
    allergens = allergens.split(", ")
    for a in allergens:
        if d.get(a) is None:
            d[a] = set(foods)
        else:
            d[a] = d[a] & set(foods)

found = dict()
added = True
while added:
    added = False
    for key in d.keys():
        d[key] = list(d[key])
        for x in d[key]:
            if x in found.values():
                d[key].remove(x)
        if len(d[key]) == 1:
            found[key] = d[key][0]
            added = True

res = [found_foods[food] for food in found_foods.keys() if food not in found.values()]
print("Part 1:", sum(res))

string = ""
for val in sorted(found):
    string += found[val] + ","
string = string[:-1]

print("Part 2:", string)
