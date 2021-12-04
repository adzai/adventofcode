with open("aoc22-input.txt") as f:
# with open("aoc22exp.txt") as f:
    lines = f.readlines()

def init_decks(lines):
    deck1 = []
    deck2 = []
    player = True
    for line in lines[1:]:
        if line == "\n":
            continue
        line = line.replace("\n", "")
        if "Player" in line:
            player = False
        elif player:
            deck1.append(int(line))
        else:
            deck2.append(int(line))
    return deck1, deck2

game_num = 1
played_games = set()
def game(deck1, deck2, turn, part2=False):
    global game_num
    current_game = game_num
    ctr = 0
    while True:
        ctr += 1
        player1 = None
        if len(deck1) == 0:
            return False
        elif len(deck2) == 0:
            return True
        elif (hsh := hash((tuple(deck1), tuple(deck2), current_game))) in played_games:
            return True
        else:
            played_games.add(hsh)
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        # print(f"Round: {ctr} Card1: {card1}, Card2: {card2}, Game: {current_game} deck1: {[card1] + deck1}, deck2: {[card2] + deck2}")
        if len(deck1) >= card1 and len(deck2) >= card2:
            game_num += 1
            player1 = game(deck1[:card1], deck2[:card2], 1, part2=part2)
        if player1 is not None and part2:
            if player1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        else:
            if card1 > card2:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)

deck1, deck2 = init_decks(lines)
game(deck1, deck2, 1)
winning_deck1 = deck2 if len(deck2) != 0 else deck1
deck1, deck2 = init_decks(lines)
game(deck1, deck2, 1, part2=True)
winning_deck2 = deck2 if len(deck2) != 0 else deck1
score1 = sum([(i + 1) * num for i, num in enumerate(winning_deck1[::-1])])
score2 = sum([(i + 1) * num for i, num in enumerate(winning_deck2[::-1])])

print("Part 1:", score1)
print("Part 2:", score2)
