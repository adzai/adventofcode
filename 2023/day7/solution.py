from collections import Counter


def parse_counts_part1(input):
    counts = []
    for line in input:
        cards, bid = line.split(" ")
        count = Counter(list(cards))
        counts.append({"score": count, "orig_cards": cards, "bid": int(bid)})

    return counts


def parse_counts_part2(input):
    counts = []
    for line in input:
        cards, bid = line.split(" ")
        count = Counter(list(cards))
        num_of_jokers = count.get("J", 0)
        del count["J"]
        if not count:
            count["J"] = 0
        count[count.most_common(1)[0][0]] += num_of_jokers
        counts.append({"score": count, "orig_cards": cards, "bid": int(bid)})

    return counts


def solve(input, part2=False):
    card_strength = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    if part2:
        card_strength["J"] = 1

    counts = parse_counts_part2(input) if part2 else parse_counts_part1(input)

    rankings = [counts[0]]
    for count in counts[1:]:
        inserted = False
        for i in range(len(rankings)):
            ranked_card_set = rankings[i]
            tie = True
            for ranked, unranked in zip(
                sorted(ranked_card_set["score"].values(), reverse=True), sorted(count["score"].values(), reverse=True)
            ):
                if ranked == unranked:
                    continue
                elif ranked > unranked:
                    rankings.insert(i, count)
                    inserted = True
                    tie = False
                    break
                else:
                    tie = False
                    break

            if tie:
                for ranked, unranked in zip(ranked_card_set["orig_cards"], count["orig_cards"]):
                    if card_strength[ranked] > card_strength[unranked]:
                        rankings.insert(i, count)
                        inserted = True
                        break
                    elif card_strength[ranked] < card_strength[unranked]:
                        break

            if inserted:
                break

        if not inserted:
            rankings.append(count)

    total_winnings = 0
    for i in range(len(rankings)):
        total_winnings += rankings[i]["bid"] * (i + 1)

    return total_winnings


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    print("Part 1:", solve(input))
    print("Part 2:", solve(input, part2=True))
