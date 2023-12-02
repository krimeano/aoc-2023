from days import SolveDay
from .game import Game


class SolveDay02x1(SolveDay):
    def solve(self, text_input: str) -> int:
        return sum(x.id for x in [Game(line) for line in self.get_lines(text_input)] if x.is_possible)


class SolveDay02x2(SolveDay):
    def solve(self, text_input: str) -> int:
        return sum(x.power for x in [Game(line) for line in self.get_lines(text_input)])
