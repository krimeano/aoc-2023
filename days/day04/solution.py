from days import SolveDay


def calculate_matches(line: str) -> int:
    [winning, have] = line.split(': ').pop().split(' | ')
    ww = set(w for w in winning.split(' ') if len(w))
    return sum(1 for h in have.split(' ') if len(h) and h in ww)


def grow_list(xx: list[int], ix: int, inc=1) -> list:
    while ix >= len(xx):
        xx.append(0)
    xx[ix] += inc
    return xx


class SolveDay04x1(SolveDay):

    def solve(self, text_input: str) -> int:
        total = 0
        for line in self.get_lines(text_input):
            matches = calculate_matches(line)
            if matches:
                total += 2 ** (matches - 1)
        return total


class SolveDay04x2(SolveDay04x1):

    def solve(self, text_input: str) -> int:
        cards = []
        ix = 0
        for line in self.get_lines(text_input):
            grow_list(cards, ix)
            matches = calculate_matches(line)
            for jy in range(ix + 1, ix + 1 + matches):
                grow_list(cards, jy, cards[ix])
            ix += 1

        return sum(cards)
