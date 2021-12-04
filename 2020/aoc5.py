with open("aoc5-input.txt") as f:
    lines = f.readlines()

highest = 0
seats = []
d = dict()
for line in lines:
    row_high = 127
    d["F"] = 127
    d["B"], d["R"] = 0, 0
    d["L"] = 7
    for char in line:
        if char not in ["R", "L"]:
            d[char] = d["B"] + (d["F"] - d["B"]) // 2
        else:
            d[char] = d["R"] + (d["L"] - d["R"]) // 2
    if highest < (seat:= d["F"] * 8 + d["L"]):
        highest = seat
    seats.append(seat)

for i in range(len((sorted_seats := sorted(seats))[8:])):
    if sorted_seats[i+1] != (found_seat := sorted_seats[i] + 1):
        break

print(f"Part 1: {highest}")
print(f"Part 2: {found_seat}")
