from .solution import SolveDay01x1, SolveDay01x2


def test_find_number():
    assert SolveDay01x1().find_number("1abc2") == '1'
    assert SolveDay01x1().find_number("pqr3stu8vwx") == '3'
    assert SolveDay01x1().find_number("a1b2c3d4e5f") == '1'
    assert SolveDay01x1().find_number("treb7uchet") == '7'


def test_find_number_backwards():
    assert SolveDay01x1().find_number("1abc2", True) == '2'
    assert SolveDay01x1().find_number("pqr3stu8vwx", True) == '8'
    assert SolveDay01x1().find_number("a1b2c3d4e5f", True) == '5'
    assert SolveDay01x1().find_number("treb7uchet", True) == '7'


def test_lines():
    assert SolveDay01x1().get_line_value("1abc2") == 12
    assert SolveDay01x1().get_line_value("pqr3stu8vwx") == 38
    assert SolveDay01x1().get_line_value("a1b2c3d4e5f") == 15
    assert SolveDay01x1().get_line_value("treb7uchet") == 77


def test_default():
    txt_input = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
    """
    expected = 142
    actual = SolveDay01x1().solve(txt_input)
    assert actual == expected


def test_find_number_2():
    assert SolveDay01x2().find_number("two1nine") == '2'
    assert SolveDay01x2().find_number("eightwothree") == '8'
    assert SolveDay01x2().find_number("abcone2threexyz") == '1'
    assert SolveDay01x2().find_number("xtwone3four") == '2'
    assert SolveDay01x2().find_number("4nineeightseven2") == '4'
    assert SolveDay01x2().find_number("zoneight234") == '1'
    assert SolveDay01x2().find_number("7pqrstsixteen") == '7'


def test_find_number_backwards_2():
    assert SolveDay01x2().find_number("two1nine", True) == '9'
    assert SolveDay01x2().find_number("eightwothree", True) == '3'
    assert SolveDay01x2().find_number("abcone2threexyz", True) == '3'
    assert SolveDay01x2().find_number("xtwone3four", True) == '4'
    assert SolveDay01x2().find_number("4nineeightseven2", True) == '2'
    assert SolveDay01x2().find_number("zoneight234", True) == '4'
    assert SolveDay01x2().find_number("7pqrstsixteen", True) == '6'


def test_lines_2():
    assert SolveDay01x2().get_line_value("two1nine") == 29
    assert SolveDay01x2().get_line_value("eightwothree") == 83
    assert SolveDay01x2().get_line_value("abcone2threexyz") == 13
    assert SolveDay01x2().get_line_value("xtwone3four") == 24
    assert SolveDay01x2().get_line_value("4nineeightseven2") == 42
    assert SolveDay01x2().get_line_value("zoneight234") == 14
    assert SolveDay01x2().get_line_value("7pqrstsixteen") == 76


def test_default_2():
    txt_input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
    expected = 281
    actual = SolveDay01x2().solve(txt_input)
    assert actual == expected
