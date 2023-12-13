from .solution import SolveDay13x1, SolveDay13x2

text_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


def test_solution_1():
    assert SolveDay13x1(True).solve(text_input) == 405


def test_solution_2():
    assert SolveDay13x2(True).solve(text_input) == 400


def test_solution_2_special():
    assert SolveDay13x2(True).solve("""
#...#######
#.#.#######
#....#.####
#....#.####
#.#.#######
#...#######
#.##.##.###
#...#...##.
##.##..##.#
###.####.##
....##.#...
""") == 100
