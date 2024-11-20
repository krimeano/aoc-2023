from .solution import SolveDay24x1, SolveDay24x2
text_input = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


def test_solution_1():
    assert SolveDay24x1(True).solve(text_input,  10, 17) == 2


def test_solution_2():
    assert SolveDay24x2(True).solve(text_input) == 0
