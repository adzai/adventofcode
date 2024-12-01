import hashlib


def part1(input):
    index = 0
    password = ""
    while True:
        result = hashlib.md5(str.encode(input + str(index)))
        print(index)
        digest = result.hexdigest()
        if digest[:5] == "00000":
            password += digest[5]
            if len(password) == 8:
                print("Part 1:", password)
                break

        index += 1


def part2(input):
    index = 0
    password = {}
    while True:
        result = hashlib.md5(str.encode(input + str(index)))
        digest = result.hexdigest()
        if digest[:5] == "00000":
            pos = digest[5]
            char = digest[6]
            if pos in "01234567" and password.get(pos) is None:
                password[pos] = char

            if len(password.keys()) == 8:
                print("Part 2:", "".join([password[char] for char in sorted(password.keys())]))
                break

        index += 1


if __name__ == "__main__":
    input = "abbhdwsy"

    part2(input)
