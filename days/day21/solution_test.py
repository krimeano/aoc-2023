from .solution import SolveDay21x1, SolveDay21x2

text_input = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def test_solution_1():
    assert SolveDay21x1(True).solve(text_input, 6) == 16


def test_solution_2():
    assert SolveDay21x2(True).solve(text_input, 6) == 16
    assert SolveDay21x2(True).solve(text_input, 10) == 50
    assert SolveDay21x2(True).solve(text_input, 50) == 1594
    assert SolveDay21x2(True).solve(text_input, 100) == 6536
    assert SolveDay21x2(True).solve(text_input, 500) == 167004
    assert SolveDay21x2(False).solve(text_input, 1000) == 668697
    assert SolveDay21x2(False).solve(text_input, 5000) == 16733044
