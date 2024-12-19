def num_of_possible_designs(patterns, design, cache):
    if cache_hit := cache.get((patterns, design)):
        return cache_hit

    if design == "":
        return 1

    total = 0
    for pattern in patterns:
        if design.startswith(pattern):
            total += num_of_possible_designs(patterns, design.replace(pattern, "", 1), cache)

    cache[(patterns, design)] = total

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n\n")
        available_patterns = tuple(input_data[0].split(", "))
        designs_to_display = input_data[1].split("\n")[:-1]

    nums_of_possible_designs = [
        num_of_possible_designs(tuple(filter(lambda pattern: pattern in design, available_patterns)), design, {})
        for design in designs_to_display
    ]
    print("Part 1:", sum(num_of_possible_designs > 0 for num_of_possible_designs in nums_of_possible_designs))
    print("Part 2:", sum(nums_of_possible_designs))
