from .solution import SolveDay18x1, SolveDay18x2
text_input = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


def test_solution_1():
    assert SolveDay18x1(True).solve(text_input) == 62


def test_solution_2():
    assert SolveDay18x2(True).solve(text_input) == 0