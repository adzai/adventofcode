import re
import math

with open("aoc13-input.txt") as f:
    lines = f.readlines()

# lines = ["939",
# "7,13,x,x,59,x,31,19"
# ]

timestamp = int(lines[0])
bus_ids = list(map(int, re.findall(r"[0-9]+", lines[1])))
smallest_diff = [timestamp, -1]
for bus_id in bus_ids:
    current_time = 0
    while current_time < timestamp:
        current_time += bus_id
    if current_time - timestamp < smallest_diff[0]:
        smallest_diff = (current_time - timestamp, bus_id)

print("PART1:", smallest_diff[0] * smallest_diff[1])
print("TS:", timestamp)
print("bi:", bus_ids)
wait_time = list(map(lambda bus_id: bus_id - timestamp % bus_id, bus_ids))
print("WAIT", wait_time)

def solve_2(data):
    data = [(i, int(bus_id))
            for i, bus_id in enumerate(data[1].split(',')) if bus_id != 'x']
    jump = data[0][1]
    time_stamp = 0
    for offset, bus_id in data[1:]:
        while (time_stamp + offset) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp

print("Part 2:", solve_2(lines))

def chinese_remainde_theorem(data):
     bus_id_mod_result = {}
     for pos, bus_id in enumerate(data[1].split(",")):
         if bus_id == 'x':
             continue
         else:
             bus_id = int(bus_id)
         bus_id_mod_result[bus_id] = (bus_id - pos) % bus_id

     total_prod = math.prod(bus_id_mod_result.keys())
     result = 0
     for bus_id, mod_result in bus_id_mod_result.items():
         bus_id_prod = total_prod // bus_id
         mod_inv = pow(bus_id_prod, -1, bus_id)
         bus_id_result = mod_result * mod_inv * bus_id_prod
         result += bus_id_result
     return result % total_prod

print("CRT:", chinese_remainde_theorem(lines))

def solve2(lines):
    data = [(int(l), i) for i, l in enumerate(lines[1].split(",")) if l != "x"]
    increment = data[0][0]
    t = 0
    for bus_id, offset in data[1:]:
        while True:
            t += increment
            if (t + offset) % bus_id == 0:
                # Don't have to use LCM since bus_ids are co-prime
                increment = increment * bus_id
                break
    return t

print("LCM:", solve2(lines))
