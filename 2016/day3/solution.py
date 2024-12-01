def is_valid_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    list_of_numbers = [
        list(map(lambda y: int(y.lstrip()), filter(lambda y: y != "", inp.lstrip().split("  ")))) for inp in input
    ]

    print(
        "Part 1:",
        sum([is_valid_triangle(*x) for x in list_of_numbers]),
    )

    num_of_valid = 0
    for i in range(0, len(list_of_numbers), 3):
        for j in range(3):
            num_of_valid += int(
                is_valid_triangle(list_of_numbers[i][j], list_of_numbers[i + 1][j], list_of_numbers[i + 2][j])
            )

    print("Part 2:", num_of_valid)
