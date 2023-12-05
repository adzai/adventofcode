def parse_maps(input):
    maps_input = input[2:]
    maps = []
    current = []
    for line in maps_input:
        if line == "":
            maps.append(current)
            current = []
        elif line[-4:-1] == "map":
            continue
        else:
            numbers = [int(x) for x in line.split(" ")]
            current.append(
                {
                    "destination_range": range(numbers[0], numbers[0] + numbers[2]),
                    "source_range": range(numbers[1], numbers[1] + numbers[2]),
                }
            )
    maps.append(current)

    return maps


def part1(seeds, maps):
    locations = []
    for seed in seeds:
        current_seed = seed
        for j, map in enumerate(maps):
            for entry in map:
                if current_seed in entry["source_range"]:
                    current_seed = entry["destination_range"][0] + current_seed - entry["source_range"][0]
                    break
            if j == len(maps) - 1:
                locations.append(current_seed)

    return min(locations)


def part2(seeds, maps):
    seed_ranges = []
    i = 0
    while i < len(seeds):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
        i += 2

    current_min = float("inf")
    rng_len = len(seed_ranges)
    for i, rng in enumerate(seed_ranges):
        print("rng:", i, "/", rng_len)
        for num in rng:
            res = part1([num], maps)
            if res < current_min:
                current_min = res

    print("Part 2:", current_min)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    seeds = [int(x) for x in input[0].replace("seeds: ", "").split(" ")]
    maps = parse_maps(input)

    print("Part 1:", part1(seeds, maps))
    part2(seeds, maps)
