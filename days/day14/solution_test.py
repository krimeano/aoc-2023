from .solution import SolveDay14x1, SolveDay14x1x2, SolveDay14x2
text_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


def test_solution_1():
    assert SolveDay14x1(False).solve(text_input) == 136


def test_solution_2():
    assert SolveDay14x1x2(False).solve(text_input) == 136
    assert SolveDay14x2(True).solve(text_input) == 64
