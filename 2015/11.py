input = "vzbxkghb"


def satisfies_rules(str):
    str_len = len(str)
    rule_1 = False
    if "i" in str or "o" in str or "l" in str:
        return False
    for i in range(max(str_len - 2, 0)):
        if ord(str[i]) == ord(str[i + 1]) - 1 == ord(str[i + 2]) - 2:
            rule_1 = True
            break
    if not rule_1:
        return False
    rule_3 = 0
    i = 0
    while i < (max(str_len - 1, 0)):
        if str[i] == str[i + 1]:
            rule_3 += 1
            if rule_3 == 2:
                return True
            i += 2
        else:
            i += 1
    return False


def increment_str(str, curr_index=-1):
    ascii_char_to_increment = ord(str[curr_index])
    lst = list(str)
    if ascii_char_to_increment == 122:
        lst[curr_index] = "a"
        return increment_str("".join(lst), curr_index=curr_index - 1)
    else:
        lst[curr_index] = chr(ascii_char_to_increment + 1)
    str = "".join(lst)
    return str


def loop(str):
    while not satisfies_rules(str):
        str = increment_str(str)
    return str


part1 = loop("vzbxkghb")
part2 = loop(increment_str(part1))
print("Part 1: ", part1)
print("Part 2: ", part2)
