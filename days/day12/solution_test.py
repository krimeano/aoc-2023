from .solution import SolveDay12x1, SolveDay12x2, can_fit, ways_to_fit

text_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


def test_can_fit():
    assert can_fit('#', 1, 0)
    assert can_fit('?', 1, 0)
    assert not can_fit('.', 1, 0)
    assert not can_fit('#', 1, 1)
    assert not can_fit('#', 2, 0)
    assert not can_fit('?', 2, 0)
    assert not can_fit('.', 2, 0)

    assert not can_fit('##', 1, 0)
    assert not can_fit('##', 1, 1)
    assert not can_fit('##', 1, 2)

    assert not can_fit('.#', 1, 0)
    assert can_fit('.#', 1, 1)
    assert not can_fit('.#', 1, 2)

    assert can_fit('#.', 1, 0)
    assert not can_fit('#.', 1, 1)
    assert not can_fit('#.', 1, 2)

    assert not can_fit('..', 1, 0)
    assert not can_fit('..', 1, 1)

    assert can_fit('??', 1, 0)
    assert can_fit('??', 1, 1)
    assert can_fit('??', 2, 0)
    assert can_fit('##', 2, 0)
    assert not can_fit('..', 2, 0)


def test_ways_to_fit():
    print()
    assert ways_to_fit('???.###', [1, 1, 3]) == 1
    assert ways_to_fit('.??..??...?##.', [1, 1, 3]) == 4
    assert ways_to_fit('?#?#?#?#?#?#?#?', [1, 3, 1, 6]) == 1
    assert ways_to_fit('????.#...#...', [4, 1, 1]) == 1
    assert ways_to_fit('????.######..#####.', [1, 6, 5]) == 4
    assert ways_to_fit('?###????????', [3, 2, 1]) == 10


def test_solution_1():
    assert SolveDay12x1(True).solve(text_input) == 21


def test_solution_2():
    assert SolveDay12x2(True).solve(text_input) == 525152
