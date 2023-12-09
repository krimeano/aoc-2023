from .solution import SolveDay09x1, SolveDay09x2

text_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""


def test_solution_1():
    assert SolveDay09x1(True).solve(text_input) == 114


def test_solution_2():
    assert SolveDay09x2(True).solve(text_input) == 2
