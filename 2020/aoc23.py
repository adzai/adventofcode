cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
cups = [3, 6, 8, 1, 9, 5, 7, 4, 2]



cup_id = 0
min_cup = min(cups)
max_cup = max(cups)
cups = cups + list(range(max_cup+1, 20000)) + list(range(9990000, 10000001))
max_cup = max(cups)
length = len(cups)
# for i in range(1000000000):
for i in range(10000000):
    print(i+1)
    # if i == 0:
    #     pass
    # elif i % 10000 == 0:
    #     cups = cups[:] + list(range(i+10000, i + 10001))
    current_cup = cups[cup_id]
    picked_up_cups = [cups[x%length] for x in range(cup_id+1, cup_id+4)]
    # print("Cups", cups)
    # print("Picked up", picked_up_cups)
    destination_candidate = current_cup - 1
    while True:
        if destination_candidate < min_cup:
            destination_candidate = max_cup
        elif destination_candidate in picked_up_cups:
            destination_candidate -= 1
        else:
            break
    # print("Dest", destination_candidate)
    for cup in picked_up_cups:
        cups.remove(cup)
    dest_index = cups.index(destination_candidate)
    cups = cups[:dest_index+1] + picked_up_cups + cups[dest_index+1:]
    cup_id = (cups.index(current_cup) + 1) % length

one_index = cups.index(1) + 1
print(cups[one_index+1] * cups[one_index+2])
# string = ""
# for _ in range(length-1):
#     string += str(cups[one_index%length])
#     one_index += 1
# print(string)
