def get_list_of_boards(board_input):
    list_of_boards = []
    d = dict()
    y = 0
    for row in board_input:
        if row == "\n":
            list_of_boards.append(d)
            d = dict()
            y = 0
        else:
            for x, elem in enumerate(row.split()):
                d[elem] = (x, y)
            y += 1

    return list_of_boards


def get_unmarked(board, winning_lst):
    unmarked_sum = 0
    for k in board.keys():
        if k not in [item for sublist in winning_lst.values() for item in sublist]:
            unmarked_sum += int(k)
    return unmarked_sum


def get_winning_seq(sequence, win_list, list_of_dicts, winning_len, part2=False):
    winners = []
    last_winner = None
    for char in sequence:
        board_num = 0
        for win_dict, board in zip(win_list, list_of_dicts):
            if board_num in winners:
                board_num += 1
                continue
            if board.get(char):
                x, y = board[char]
                x = "ROW: " + str(x)
                y = "COL: " + str(y)
                if win_dict.get(x) and char not in win_dict[x]:
                    win_dict[x] += [char]
                else:
                    win_dict[x] = [char]
                if win_dict.get(y) and char not in win_dict[y]:
                    win_dict[y] += [char]
                else:
                    win_dict[y] = [char]
                if len(win_dict[x]) == winning_len or len(win_dict[y]) == winning_len:
                    winners.append(board_num)
                    winning_num = int(char)
                    last_winner = winning_num * get_unmarked(board, win_dict)
                    if not part2:
                        return last_winner
            board_num += 1
    return last_winner


if __name__ == "__main__":
    with open("4.input") as f:
        lines = f.readlines()

    sequence = lines[0].split(",")
    board_input = lines[2:] + ["\n"]
    winning_len = len(board_input[0].split())
    list_of_boards = get_list_of_boards(board_input)
    win_list = [dict() for _ in list_of_boards]

    print("Part 1:", get_winning_seq(sequence, win_list, list_of_boards, winning_len))
    print(
        "Part 2:",
        get_winning_seq(sequence, win_list, list_of_boards, winning_len, part2=True),
    )
