from days import SolveDay


class SolveDay08x1(SolveDay):
    route: list[int] = []
    nodes: dict[tuple[str, str]] = {}

    def solve(self, text_input: str) -> int:
        self.parse_lines(self.get_lines(text_input))
        if self.verbose:
            print(self.route)
            print(self.nodes)
        return self.crawl()

    def parse_lines(self, lines: list[str]):
        self.route = [x == 'R' and 1 or 0 for x in lines.pop(0)]
        self.nodes = {z[0]: (z[1][0], z[1][1]) for z in [(y[0], y[1][1:-1].split(', ')) for y in [x.split(' = ') for x in lines]]}

    def crawl(self) -> int:
        ix = 0
        size = len(self.route)
        current = 'AAA'
        while current != 'ZZZ':
            if self.verbose:
                print('{:>5}'.format(ix + 1), '{:>3}'.format(ix % size), self.route[ix % size] and 'R' or 'L', current, end=' -> ')
            current = self.nodes[current][self.route[ix % size]]
            if self.verbose:
                print(current)
            ix += 1
        return ix


class SolveDay08x2(SolveDay08x1):
    def solve(self, text_input: str) -> int:
        return 0
