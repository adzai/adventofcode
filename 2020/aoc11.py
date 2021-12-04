with open("aoc11-input.txt") as f:
    lines = f.readlines()

# lines = ["L.LL.LL.LL",
# "LLLLLLL.LL",
# "L.L.L..L..",
# "LLLL.LL.LL",
# "L.LL.LL.LL",
# "L.LLLLL.LL",
# "..L.L.....",
# "LLLLLLLLLL",
# "L.LLLLLL.L",
# "L.LLLLL.LL",
# ]

def occupy_seat(row, col, lines):
    lst = []
    rr = row - 1 if row - 1 >= 0 else 0
    cc = col - 1 if col - 1 >= 0 else 0
    row_range = range(rr, row+2)
    col_range = range(cc, col+2)
    for i in row_range:
        for j in col_range:
            if i == row and j == col:
                continue
            try: lst.append(lines[i][j])
            except:
                pass
    return False if "#" in lst else True

def empty_seat(row, col, lines):
    lst = []
    rr = row - 1 if row - 1 >= 0 else 0
    cc = col - 1 if col - 1 >= 0 else 0
    row_range = range(rr, row+2)
    col_range = range(cc, col+2)
    length = 0
    for i in row_range:
        for j in col_range:
            if i == row and j == col:
                continue
            try:
                lst.append(lines[i][j])
            except:
                pass
    ctr = 0
    for item in lst:
        if item == "#":
            ctr += 1
    return True if ctr >= 4 else False

def count_occ_seats(lines):
    ctr = 0
    for line in lines:
        for char in line:
            if "#" in char:
                ctr += 1
    return ctr

def move_vertically(lines,row, col):
    temp_row = row + 1
    lst = []
    # right
    while temp_row >= 0 and temp_row < len(lines):
        if lines[temp_row][col] == ".":
            pass
        else:
            lst.append(lines[temp_row][col])
            break
        temp_row += 1
    # right
    temp_row = row - 1
    while temp_row >= 0 and temp_row < len(lines):
        if lines[temp_row][col] == ".":
            pass
        else:
            lst.append(lines[temp_row][col])
            break
        temp_row -= 1
    return lst

def move_horizontally(lines,row, col):
    temp_col = col + 1
    lst = []
    # right
    while temp_col >= 0 and temp_col < len(lines[0]):
        if lines[row][temp_col] == ".":
            pass
        else:
            lst.append(lines[row][temp_col])
            break
        temp_col += 1
    # right
    temp_col = col - 1
    while temp_col >= 0 and temp_col < len(lines[0]):
        if lines[row][temp_col] == ".":
            pass
        else:
            lst.append(lines[row][temp_col])
            break
        temp_col -= 1
    return lst


def move_diagonally(lines, row, col):
    lst = []
    temp_row = row + 1
    temp_col = col + 1
    l_r = len(lines)
    l_c = len(lines[0])
    while (temp_row >= 0 and temp_row < l_r) and (temp_col >= 0 and temp_col < l_c):
        if lines[temp_row][temp_col] == ".":
            pass
        else:
            lst.append(lines[temp_row][temp_col])
            break
        temp_row += 1
        temp_col += 1
    temp_row = row - 1
    temp_col = col + 1
    # down and left
    while (temp_row >= 0 and temp_row < l_r) and (temp_col >= 0 and temp_col < l_c):
        if lines[temp_row][temp_col] == ".":
            pass
        else:
            lst.append(lines[temp_row][temp_col])
            break
        temp_row -= 1
        temp_col += 1
    temp_row = row + 1
    temp_col = col - 1
    # up and right
    while (temp_row >= 0 and temp_row < l_r) and (temp_col >= 0 and temp_col < l_c):
        if lines[temp_row][temp_col] == ".":
            pass
        else:
            lst.append(lines[temp_row][temp_col])
            break
        temp_row += 1
        temp_col -= 1
    temp_row = row - 1
    temp_col = col - 1
    # up and left
    while (temp_row >= 0 and temp_row < l_r) and (temp_col >= 0 and temp_col < l_c):
        if lines[temp_row][temp_col] == ".":
            pass
        else:
            lst.append(lines[temp_row][temp_col])
            break
        temp_row -= 1
        temp_col -= 1
    return lst


def part1(lines):
    prev_lines = lines
    while True:
        new_lines = []
        for i in range(len(prev_lines)):
            lst = []
            for j in range(len(prev_lines[i])):
                symbol = prev_lines[i][j]
                if symbol == "\n":
                    break
                if symbol == "L":
                    if occupy_seat(i, j, prev_lines):
                        lst.append("#")
                    else:
                        lst.append(symbol)
                elif symbol == "#":
                    if empty_seat(i, j, prev_lines):
                        lst.append("L")
                    else:
                        lst.append(symbol)
                else:
                    lst.append(symbol)

            new_lines.append(lst)
        if new_lines == prev_lines:
            print("END")
            break
        else:
            prev_lines = new_lines
    return new_lines

def part2(lines):
    prev_lines = lines
    ctr = 0
    while True:
        new_lines = []
        for i in range(len(prev_lines)):
            lst = []
            for j in range(len(prev_lines[i])):
                symbol = prev_lines[i][j]
                if symbol == "\n":
                    break
                if symbol == "L":
                    diag = move_diagonally(prev_lines, i, j)
                    horiz = move_horizontally(prev_lines, i, j)
                    vert = move_vertically(prev_lines, i, j)
                    res = diag + horiz + vert
                    if "#" in res:
                        lst.append(symbol)
                    else:
                        lst.append("#")
                elif symbol == "#":
                    diag = move_diagonally(prev_lines, i, j)
                    horiz = move_horizontally(prev_lines, i, j)
                    vert = move_vertically(prev_lines, i, j)
                    cnt = 0
                    res = diag + horiz + vert
                    for s in res:
                        if s == "#":
                            cnt += 1
                    if cnt >= 5:
                        lst.append("L")
                    else:
                        lst.append(symbol)
                else:
                    lst.append(symbol)

            new_lines.append(lst)
        # ctr += 1
        # for line in new_lines:
        #     print("".join(line))
        # print("============")
        # if ctr == 2:
        #     break
        if new_lines == prev_lines:
            print("END")
            break
        else:
            prev_lines = new_lines
    return new_lines

new_lines = part1(lines)
print(count_occ_seats(new_lines))
newer_lines = part2(lines)
print(count_occ_seats(newer_lines))
