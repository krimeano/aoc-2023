from days import SolveDay
from .progression import Progression


class SolveDay09x1(SolveDay):

    def solve(self, text_input: str) -> int:
        return sum(Progression([int(x) for x in line.split(' ')]).next() for line in self.get_lines(text_input))


class SolveDay09x2(SolveDay09x1):
    def solve(self, text_input: str) -> int:
        return sum(Progression([int(x) for x in line.split(' ')]).prev() for line in self.get_lines(text_input))
