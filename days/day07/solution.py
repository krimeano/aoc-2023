from days import SolveDay
from .hand import Hand
from .hand_joker import HandJoker


class SolveDay07x1(SolveDay):
    def solve(self, text_input: str) -> int:
        if self.verbose:
            print()

        hands: list[Hand] = sorted([self.get_hand(line) for line in self.get_lines(text_input)], key=lambda x: x.sorting)

        return sum((ix + 1) * hands[ix].bid for ix in range(len(hands)))

    def get_hand(self, line) -> Hand:
        return Hand(*line.split(' '))


class SolveDay07x2(SolveDay07x1):
    def get_hand(self, line) -> HandJoker:
        return HandJoker(*line.split(' '))
