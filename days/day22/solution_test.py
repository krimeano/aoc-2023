from .solution import SolveDay22x1, SolveDay22x2

text_input = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""


def test_solution_1():
    assert SolveDay22x1(True).solve(text_input) == 5


def test_solution_2():
    assert SolveDay22x2(True).solve(text_input) == 7
