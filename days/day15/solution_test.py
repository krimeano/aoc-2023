from .solution import SolveDay15x1, SolveDay15x2

text_input = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""


def test_solution_1():
    assert SolveDay15x1(True).solve(text_input) == 1320


def test_solution_2():
    assert SolveDay15x2(True).solve(text_input) == 0
