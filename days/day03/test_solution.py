from .solution import SolveDay03x1, SolveDay03x2

text_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_solution_1():
    assert SolveDay03x1(False).solve(text_input) == 4361


def test_solution_2():
    assert SolveDay03x2(True).solve(text_input) == 467835
