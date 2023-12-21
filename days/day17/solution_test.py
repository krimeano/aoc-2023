from .solution import SolveDay17x1, SolveDay17x2

text_input = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""


def test_solution_1():
    assert SolveDay17x1(True).solve(text_input) == 102


def test_solution_2():
    assert SolveDay17x2(True).solve(text_input) == 94
