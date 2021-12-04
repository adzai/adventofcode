input = 3113322113


def process_sequence(seq):
    current_num = None
    current_sum = 0
    new_seq = []
    for num in seq:
        if current_num is None:
            current_num = num
            current_sum += 1
        elif current_num != num:
            new_seq.append(current_sum)
            new_seq.append(current_num)
            current_num = num
            current_sum = 1
        else:
            current_sum += 1

    new_seq.append(current_sum)
    new_seq.append(current_num)
    return new_seq


seq1 = list(map(int, [char for char in str(input)]))
for _ in range(40):
    seq1 = process_sequence(seq1)

seq2 = list(map(int, [char for char in str(input)]))
for _ in range(50):
    seq2 = process_sequence(seq2)

print("Part 1: ", len(seq1))
print("Part 2: ", len(seq2))
