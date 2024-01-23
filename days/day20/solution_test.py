from .solution import SolveDay20x1, SolveDay20x2

text_input = """
"""


def test_solution_1():
    assert SolveDay20x1(True).solve("""
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""") == 32000000

    assert SolveDay20x1(True).solve("""
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""") == 11687500
