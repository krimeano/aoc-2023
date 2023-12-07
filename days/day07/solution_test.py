from .solution import SolveDay07x1, SolveDay07x2
text_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


def test_solution_1():
    assert SolveDay07x1(True).solve(text_input) == 6440


def test_solution_2():
    assert SolveDay07x2(True).solve(text_input) == 5905
