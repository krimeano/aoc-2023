from .game import Game

# in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively

test_cases = [
    ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True, 48],
    ["Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True, 12],
    ["Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False, 1560],
    ["Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False, 630],
    ["Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True, 36]
]


def test_games():
    for [line, is_possible, power] in test_cases:
        game = Game(line)
        assert game.is_possible == is_possible
        assert game.power == power
