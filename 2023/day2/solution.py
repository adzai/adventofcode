from collections import defaultdict

with open("input.txt") as f:
    games = f.read().split("\n")[:-1]


def get_rounds_configuration(round):
    cubes = round.split(", ")
    round_configuration = defaultdict(int)
    for cube in cubes:
        number, color = cube.split(" ")
        round_configuration[color] += int(number)

    return round_configuration


def parse_game(game):
    game_id_txt, plays = game.split(": ")
    game_id = game_id_txt.split(" ")[-1]
    rounds = plays.split(";")
    rounds = [round.lstrip() for round in rounds]

    return int(game_id), rounds


def is_game_valid(rounds, cfg):
    game_is_valid = True
    for round in rounds:
        rounds_configuration = get_rounds_configuration(round)
        for color, number in rounds_configuration.items():
            if number > cfg[color]:
                game_is_valid = False
                break
        if not game_is_valid:
            break

    return game_is_valid


def get_game_power(rounds):
    game_cfg = defaultdict(int)
    for round in rounds:
        rounds_configuration = get_rounds_configuration(round)
        for color, number in rounds_configuration.items():
            if number > game_cfg[color]:
                game_cfg[color] = number

    power = 1
    for number in game_cfg.values():
        power *= number

    return power


def part1():
    cfg = {"red": 12, "green": 13, "blue": 14}
    valid_ids = []
    for game in games:
        game_id, rounds = parse_game(game)
        if is_game_valid(rounds, cfg):
            valid_ids.append(game_id)

    print("Part 1:", sum(valid_ids))


def part2():
    powers = 0
    for game in games:
        _, rounds = parse_game(game)
        powers += get_game_power(rounds)

    print("Part 2:", powers)


part1()
part2()
