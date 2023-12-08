from days import SolveDay

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149)


class SolveDay08x1(SolveDay):
    route: list[int] = []
    nodes: dict[tuple[str, str]] = {}

    def solve(self, text_input: str) -> int:
        self.parse_lines(self.get_lines(text_input))
        if self.verbose:
            print(self.route)
            print(self.nodes)
        return self.run()

    def parse_lines(self, lines: list[str]):
        self.route = [x == 'R' and 1 or 0 for x in lines.pop(0)]
        self.nodes = {z[0]: (z[1][0], z[1][1]) for z in [(y[0], y[1][1:-1].split(', ')) for y in [x.split(' = ') for x in lines]]}

    def run(self) -> int:
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
    def run(self) -> int:
        all_factors = set()
        for node in [x for x in self.nodes.keys() if x[-1] == 'A']:
            cycle_data = self.find_cycle(node)
            cycle = cycle_numbers(cycle_data)
            ff = find_factors(cycle[0])
            for f in ff:
                all_factors.add(f)
        print(all_factors)
        result = 1
        for f in all_factors:
            result *= f
        return result

    def find_cycle(self, node: str) -> tuple[list[str], list[str]]:
        body = []

        current = node
        ix = 0
        size = len(self.route)
        ix_mod_size = ix % size
        visited = set()

        while (current, ix_mod_size) not in visited:
            visited.add((current, ix_mod_size))
            body.append(current)
            current = self.nodes[current][self.route[ix % size]]
            ix += 1
            ix_mod_size = ix % size
        pos = body.index(current)
        return body[:pos], body[pos:]


def cycle_numbers(cycle: tuple[list[str], list[str]]) -> tuple[int, list[int]]:
    head, body = cycle
    indexes = [ix + len(head) for ix in range(len(body)) if body[ix][-1] == 'Z']
    return len(body), indexes


def find_factors(n: int) -> list[int]:
    out = []
    m = n
    r = m ** 0.5
    for ix in range(len(PRIMES)):
        p = PRIMES[ix]
        if p > r:
            break
        if not m % p:
            out.append(p)
            m = m // p
            r = m ** 0.5

    out.append(m)

    return out
