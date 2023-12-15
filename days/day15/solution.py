from functools import reduce

from days import SolveDay


class SolveDay15x1(SolveDay):

    def solve(self, text_input: str) -> int:
        return sum(reduce(lambda h, x: ((h + x) * 17) % 256, [0] + [ord(c) for c in cc]) for cc in self.get_lines(text_input).pop().split(','))


class SolveDay15x2(SolveDay15x1):

    def solve(self, text_input: str) -> int:
        return 0
