VALID_DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def is_char_a_number(n):
    try:
        int(n)
        return True

    except ValueError:
        return False


def get_indexes_of_found_letter_digits(input):
    ret = {}
    for i, digit in enumerate(VALID_DIGITS):
        n = 0
        idx = 0
        while n != -1:
            n = input.find(digit, idx)
            if n == -1:
                continue

            ret[n] = str(i + 1)
            idx = n + 1

    return ret


def get_indexes_of_found_numerical_digits(input):
    ret = {}
    for i, char in enumerate(input):
        if is_char_a_number(char):
            ret[i] = char

    return ret


def solution(inputs, part2):
    total_sum = 0
    for input in inputs:
        found_numericals = get_indexes_of_found_numerical_digits(input)
        found_spelled_out_numbers = get_indexes_of_found_letter_digits(input) if part2 else {}

        min_numerical = min(found_numericals.keys()) if found_numericals else float("inf")
        max_numerical = max(found_numericals.keys()) if found_numericals else float("-inf")

        min_spelled_out = min(found_spelled_out_numbers.keys()) if found_spelled_out_numbers else float("inf")
        max_spelled_out = max(found_spelled_out_numbers.keys()) if found_spelled_out_numbers else float("-inf")

        first_number = (
            found_numericals[min_numerical]
            if min_numerical < min_spelled_out
            else found_spelled_out_numbers[min_spelled_out]
        )
        second_number = (
            found_numericals[max_numerical]
            if max_numerical > max_spelled_out
            else found_spelled_out_numbers[max_spelled_out]
        )

        total_sum += int(first_number + second_number)

    return total_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        inputs = f.read().split("\n")[:-1]

    print("Part 1:", solution(inputs, part2=False))
    print("Part 2:", solution(inputs, part2=True))
