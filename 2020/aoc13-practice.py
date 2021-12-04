import re

with open("aoc13-input.txt") as f:
    lines = f.readlines()

# lines = ["939",
# "7,13,x,x,59,x,31,19"
# ]
timestamp = int(lines[0])
bus_ids = list(map(int, re.findall(r"[0-9]+", lines[1])))
# Find remainder and then found how much till the next 0 mod occurs
time_till_next = list(map(lambda bus_id:
                          bus_id - (timestamp % bus_id), bus_ids))

smallest = [time_till_next[0], bus_ids[0]]
for i in range(len(time_till_next)):
    if time_till_next[i] < smallest[0]:
        smallest = [time_till_next[i], bus_ids[i]]

print("Part1:", smallest[0] * smallest[1])


bus_ids = [(int(bus_id), offset)
           for offset, bus_id in enumerate(lines[1].split(",")) if bus_id != "x"]


jump = bus_ids[0][0]
t = jump
for bus_id, offset in bus_ids[1:]:
    while True:
        if (t + offset) % bus_id == 0:
            jump *= bus_id
            break
        else:
            t += jump

print("Part2:", t)
