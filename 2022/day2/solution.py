from dataclasses import dataclass

with open("input.txt") as f:
    strategy_guide = f.readlines()


@dataclass(frozen=True)
class Shape:
    opponent_shape: str
    my_shape: str
    value: int

    def get_shapes(self):
        return [self.opponent_shape, self.my_shape]


class Game:
    def __init__(self, strategy_guide):
        self.strategy_guide = strategy_guide
        self.rock = Shape("A", "X", 1)
        self.paper = Shape("B", "Y", 2)
        self.scissors = Shape("C", "Z", 3)
        self.player1_score = 0
        self.player2_score = 0
        self.winner_lookup_table = {
            self.rock: {self.scissors: 1, self.paper: -1, self.rock: 0},
            self.paper: {self.rock: 1, self.scissors: -1, self.paper: 0},
            self.scissors: {self.paper: 1, self.rock: -1, self.scissors: 0},
        }

    def get_shape(self, shape):
        shape = shape.strip()
        if shape in self.rock.get_shapes():
            return self.rock
        elif shape in self.paper.get_shapes():
            return self.paper
        elif shape in self.scissors.get_shapes():
            return self.scissors
        else:
            raise Exception("Shape not found")

    def decide_shape_to_play(self, opponent_shape, symbol):
        if symbol == "X":
            target_value = 1
        elif symbol == "Y":
            target_value = 0
        else:
            target_value = -1
        possibilities = self.winner_lookup_table[opponent_shape]
        for k, v in possibilities.items():
            if v == target_value:
                return k
        raise Exception("Did not find correct shape to play")

    def decide_winner(self, shape1, shape2):
        return self.winner_lookup_table[shape1][shape2]

    def play_turn(self, player1_shape, player2_shape, part2):
        if part2:
            player2_shape = self.decide_shape_to_play(player1_shape, player2_shape.my_shape)
        result = self.decide_winner(player1_shape, player2_shape)
        self.player1_score += player1_shape.value
        self.player2_score += player2_shape.value
        if result > 0:
            self.player1_score += 6
        elif result < 0:
            self.player2_score += 6
        else:
            self.player1_score += 3
            self.player2_score += 3

    def play_new_game(self, part2=False):
        self.player1_score = 0
        self.player2_score = 0
        for turn in self.strategy_guide:
            opponent_shape, my_shape = turn.split(" ")
            opponent_shape = self.get_shape(opponent_shape)
            my_shape = self.get_shape(my_shape)
            self.play_turn(opponent_shape, my_shape, part2=part2)


game = Game(strategy_guide)

game.play_new_game()
print("Part 1:", game.player2_score)

game.play_new_game(part2=True)
print("Part 2:", game.player2_score)
