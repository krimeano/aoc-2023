from days import SolveDay
from .hand import Hand


class SolveDay07x1(SolveDay):
    with_jokers = False

    def solve(self, text_input: str) -> int:
        if self.verbose:
            print()

        hands: list[Hand] = sorted([Hand(self.with_jokers, *line.split(' ')) for line in self.get_lines(text_input)], key=lambda x: x.sorting)

        return sum((ix + 1) * hands[ix].bid for ix in range(len(hands)))


class SolveDay07x2(SolveDay07x1):
    with_jokers = True
