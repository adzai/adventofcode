import itertools
from typing import Literal


def solve(input, available_operators: list[Literal["+", "*", "||"]]):
    result = 0
    for line in input:
        lhs, rhs = line.split(": ")
        lhs = int(lhs)
        nums = list(map(lambda num: int(num), rhs.split(" ")))

        all_possible_operations = itertools.product(available_operators, repeat=(len(nums) - 1))
        for operation_sequence in all_possible_operations:
            local_result = nums[0]
            for i, operator in enumerate(operation_sequence):
                match operator:
                    case "+":
                        local_result = local_result + nums[i + 1]
                    case "*":
                        local_result = local_result * nums[i + 1]
                    case "||":
                        local_result = int(str(local_result) + str(nums[i + 1]))

            if local_result == lhs:
                result += lhs
                break

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    print("Part 1:", solve(input, ["+", "*"]))
    print("Part 2:", solve(input, ["+", "*", "||"]))
