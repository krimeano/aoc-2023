from .solution import SolveDay08x1, SolveDay08x2

text_input = """
"""


def test_solution_1():
    assert SolveDay08x1(True).solve("""
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""") == 2

    assert SolveDay08x1(True).solve("""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""") == 6


def test_solution_2():
    assert SolveDay08x2(True).solve(text_input) == 0
