from .solution import SolveDay03x1


def test_solution_1():
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
    assert SolveDay03x1(True).solve(text_input) == 4361
