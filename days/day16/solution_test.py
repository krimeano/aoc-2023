from .solution import SolveDay16x1, SolveDay16x2

text_input = """
.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""


def test_solution_1():
    assert SolveDay16x1(True).solve(text_input) == 46


def test_solution_2():
    assert SolveDay16x2(True).solve(text_input) == 51
