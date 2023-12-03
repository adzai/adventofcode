with open("input.txt") as f:
    engine_schema = f.read().split("\n")[:-1]


def parse_numbers(line):
    current_number = ""
    parsing_number = False
    start_idx = -1
    parsed_numbers = {}
    for i, char in enumerate(line):
        if char.isnumeric() and not parsing_number:
            start_idx = i

        if char.isnumeric():
            parsing_number = True
            current_number += char
        elif parsing_number:
            parsing_number = False
            parsed_numbers[(int(current_number), (start_idx, i))] = (start_idx, i)
            current_number = ""

    if parsing_number:
        parsed_numbers[(int(current_number), (start_idx, len(line)))] = (start_idx, len(line))

    return parsed_numbers


def get_numbers_to_check():
    indexes_to_check = []
    for i, line in enumerate(engine_schema):
        parsed_numbers = parse_numbers(line)
        for num_pair, index_range in parsed_numbers.items():
            num = num_pair[0]
            indexes = []
            for index in range(index_range[0], index_range[1]):
                indexes.append({"col": i, "row": index})
            indexes_to_check.append({"number": num, "indexes": indexes})

    return indexes_to_check


def check_symbol(col, row, engine_schema, condition):
    if col < 0 or row < 0:
        return False

    try:
        symbol = engine_schema[col][row]

        return condition(symbol)
    except IndexError:
        return False


def check_all_possible_symbols(col, row, engine_schema, indexes_to_skip, condition):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (col + i, row + j) not in indexes_to_skip:
                if check_symbol(col + i, row + j, engine_schema, condition):
                    return (col + i, row + j)

    return False


def get_all_checks(numbers_to_check, condition):
    all_checks = []
    for number in numbers_to_check:
        checks = []
        indexes_to_skip = [(i["col"], i["row"]) for i in number["indexes"]]
        for indexes in number["indexes"]:
            checks.append(
                check_all_possible_symbols(indexes["col"], indexes["row"], engine_schema, indexes_to_skip, condition)
            )

        all_checks.append((checks, number["number"]))

    return all_checks


def part1(numbers_to_check):
    sum = 0
    all_checks = get_all_checks(numbers_to_check, lambda symbol: symbol != ".")
    for checks_for_numbers in all_checks:
        number = checks_for_numbers[1]
        if any(checks_for_numbers[0]):
            sum += number

    print("Part 1:", sum)


def part2(numbers_to_check):
    all_checks = get_all_checks(numbers_to_check, lambda symbol: symbol == "*")
    candidate_gears = {}
    gears = {}
    for checks_for_numbers in all_checks:
        number = checks_for_numbers[1]
        for check in checks_for_numbers[0]:
            if check:
                if candidate_gears.get(check) is None:
                    candidate_gears[check] = number
                elif candidate_gears.get(check):
                    gears[check] = candidate_gears[check] * number
                    candidate_gears[check] = False
                break

    print("Part 2:", sum(gears.values()))


if __name__ == "__main__":
    numbers_to_check = get_numbers_to_check()
    part1(numbers_to_check)
    part2(numbers_to_check)
