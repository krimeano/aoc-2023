from enum import IntEnum

from days import SolveDay

"""

  N
W   E
  S

"""


class Direction(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


Quant = tuple[int, int, Direction]

SHIFT = {
    Direction.N: (-1, 0),
    Direction.E: (0, 1),
    Direction.S: (1, 0),
    Direction.W: (0, -1)
}

CELLS = {
    '\\': {
        Direction.N: [Direction.W],
        Direction.E: [Direction.S],
        Direction.S: [Direction.E],
        Direction.W: [Direction.N],
    },
    '/': {
        Direction.N: [Direction.E],
        Direction.E: [Direction.N],
        Direction.S: [Direction.W],
        Direction.W: [Direction.S],
    },
    '-': {
        Direction.N: [Direction.E, Direction.W],
        Direction.S: [Direction.E, Direction.W],
    },
    '|': {
        Direction.E: [Direction.N, Direction.S],
        Direction.W: [Direction.N, Direction.S],
    }
}


def trace(quant: Quant, cell: str) -> list[Quant]:
    y, x, d = quant

    if cell in CELLS:
        if d in CELLS[cell]:
            return [(y + SHIFT[e][0], x + SHIFT[e][1], e) for e in CELLS[cell][d]]

    dy, dx = SHIFT[d]
    return [(y + dy, x + dx, d)]


class SolveDay16x1(SolveDay):
    cells: list[list[str]]
    size: int
    energized: list[list[int]]
    trace_q: list[Quant]
    visited: set[Quant]

    def solve(self, text_input: str) -> int:
        self.parse_data(text_input).reset().trace()
        if self.verbose:
            self.print()
        return self.measure()

    def parse_data(self, text_input: str):
        self.cells = [[c for c in line] for line in self.get_lines(text_input)]
        self.size = len(self.cells)
        return self

    def reset(self, y=0, x=0, d=Direction.E):
        self.energized = [[0] * self.size for _ in range(self.size)]

        self.trace_q: list[Quant] = []
        self.visited = set()
        self.add_quant((y, x, d))
        return self

    def trace(self):
        while self.trace_q:
            current = self.trace_q.pop()
            y0, x0, d0 = current
            self.energized[y0][x0] += 1
            children = trace(current, self.cells[y0][x0])
            if self.verbose:
                print(current, '->', children)
            for child in children:
                self.add_quant(child)
        return self

    def measure(self):
        return sum([sum([1 for x in xx if x]) for xx in self.energized])

    def add_quant(self, quant: Quant) -> bool:
        y, x, d = quant
        if 0 <= y < self.size and 0 <= x < self.size and quant not in self.visited:
            self.trace_q.append(quant)
            self.visited.add(quant)
            return True
        return False

    def print(self):
        print('\n'.join(''.join(cc) for cc in self.cells) + '\n')
        print('\n'.join(''.join(e and '#' or '.' for e in ee) for ee in self.energized) + '\n')


class SolveDay16x2(SolveDay16x1):

    def solve(self, text_input: str) -> int:
        self.parse_data(text_input)

        max_energy = 0

        start = ([(ix, 0, Direction.E) for ix in range(self.size)]
                 + [(0, ix, Direction.S) for ix in range(self.size)]
                 + [(ix, self.size - 1, Direction.W) for ix in range(self.size)]
                 + [(self.size - 1, ix, Direction.N) for ix in range(self.size)])

        for y, x, d in start:
            energy = self.reset(y, x, d).trace().measure()
            if energy > max_energy:
                max_energy = energy

        return max_energy
