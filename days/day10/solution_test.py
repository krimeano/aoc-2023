from .solution import SolveDay10x1, SolveDay10x2
text_input = """
"""


def test_solution_1():
    assert SolveDay10x1(True).solve("""
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
""") == 4
    assert SolveDay10x1(True).solve("""
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
""") == 8


def test_solution_2():
    assert SolveDay10x2(True).solve(text_input) == 0
