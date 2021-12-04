cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
# cups = [3, 6, 8, 1, 9, 5, 7, 4, 2]



cup_id = 0
min_cup = min(cups)
max_cup = max(cups)
# cups = cups + list(range(max_cup+1, 10000001))
length = len(cups)
# for i in range(1000000000):
for i in range(10):
    print(i+1)
    current_cup = cups[cup_id]
    picked_up_cups = [cups[x%length] for x in range(cup_id+1, cup_id+4)]
    picked_id_start = (cup_id+1) % length
    picked_id_finish = (cup_id+3) % length
    print("Picked", picked_id_start)
    # print("Cups", cups)
    print("Picked up", picked_up_cups)
    destination_index = length - 1
    amt = -1
    while current_cup + amt in picked_up_cups:
        amt -= 1
    print(current_cup)
    print("amt", current_cup-amt)
    while True:
        if destination_index < 0:
            destination_index = length - 1
            break
        elif destination_index in (picked_id_start, (picked_id_start + 1) % length, picked_id_finish):
            destination_index -= 1
        elif cups[destination_index] == current_cup + amt:
            print(cups[destination_index])
            break
        else:
            destination_index -= 1
    print("Dest", cups[destination_index])
    print(cups)
    print(picked_id_finish)
    if picked_id_finish > destination_index:
        cups = cups[:destination_index+1] + cups[picked_id_start:picked_id_finish+1] + cups[destination_index+1:picked_id_start] + cups[picked_id_finish+1:]
    # dest_index = cups.index(destination_candidate)
        # cups = cups[picked_id_finish:destination_index+1] + cups[picked_id_start:]
    else:
        cups = cups[:picked_id_start] + cups[picked_id_finish+1:destination_index+1] + cups[picked_id_start:picked_id_finish+1] + cups[destination_index+1:]
        # cups = cups[:picked_id_start] + cups[picked_id_finish+1:destination_index+1] + cups[picked_id_start:picked_id_finish+1] + cups[destination_index+1:]
    print(cups)
    cup_id = (cups.index(current_cup) + 1) % length

one_index = cups.index(1) + 1
string = ""
for _ in range(length-1):
    string += str(cups[one_index%length])
    one_index += 1
print(string)
