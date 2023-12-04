from collections import defaultdict


def parse_card(card):
    card_split = card.split(": ")
    card_num = int(card_split[0].replace("Card ", ""))
    numbers = card_split[1]
    winning_numbers, my_numbers = numbers.split(" | ")
    winning_numbers = [int(x.lstrip()) for x in winning_numbers.split(" ") if x != ""]
    my_numbers = [int(x.lstrip()) for x in my_numbers.split(" ") if x != ""]

    return card_num, winning_numbers, my_numbers


def part1(input):
    total_points = 0
    for card in input:
        _, winning_numbers, my_numbers = parse_card(card)
        current_card_points = 0
        for number in my_numbers:
            if number in winning_numbers:
                if current_card_points:
                    current_card_points *= 2
                else:
                    current_card_points = 1

        total_points += current_card_points

    print("Part 1:", total_points)


def part2(input):
    num_of_times_to_process = defaultdict(int)
    for card in input:
        card_num, winning_numbers, my_numbers = parse_card(card)
        num_of_times_to_process[card_num] += 1
        card_num, winning_numbers, my_numbers = parse_card(card)
        total_won = 0
        for number in my_numbers:
            if number in winning_numbers:
                total_won += 1

        for i in range(card_num + 1, card_num + 1 + total_won):
            num_of_times_to_process[i] += num_of_times_to_process[card_num]

    print("Part 2:", sum(num_of_times_to_process.values()))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    part1(input)
    part2(input)
