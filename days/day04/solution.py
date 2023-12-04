from days import SolveDay


class SolveDay04x1(SolveDay):

    def solve(self, text_input: str) -> int:
        total = 0
        for line in self.get_lines(text_input):
            parts = line.split(':').pop().split('|')
            ww = set(w for w in parts[0].split(' ') if len(w))
            points = sum(1 for x in parts[1].split(' ') if len(x) and x in ww)

            if points:
                total += 2 ** (points - 1)
        return total


class SolveDay04x2(SolveDay04x1):

    def solve(self, text_input: str) -> int:
        return 0
