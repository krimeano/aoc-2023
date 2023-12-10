from enum import IntEnum

from days import SolveDay


class Side(IntEnum):
    G = 0
    N = 1
    E = 1 << 1
    S = 1 << 2
    W = 1 << 3


SHIFT = {
    Side.N: (-1, 0),
    Side.E: (0, 1),
    Side.S: (1, 0),
    Side.W: (0, -1)
}

NEIGHBOURS = {
    Side.N: Side.S,
    Side.E: Side.W,
    Side.S: Side.N,
    Side.W: Side.E,
}

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
PIPES = {
    '|': Side.N | Side.S,
    '-': Side.E | Side.W,
    'L': Side.N | Side.E,
    'J': Side.N | Side.W,
    '7': Side.S | Side.W,
    'F': Side.S | Side.E,
    '.': Side.G,
    'S': Side.N.value | Side.S.value | Side.E.value | Side.W.value
}


class SolveDay10x1(SolveDay):
    pipes: list[str]
    height: int
    width: int
    s: tuple[int, int]
    loop: list[tuple[int, int]]

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input)
        if self.verbose:
            print(self.loop)
        return len(self.loop) // 2

    def parse_input(self, text_input: str):
        if self.verbose:
            print(text_input)
        self.pipes = self.get_lines(text_input)
        self.height = len(self.pipes)
        self.width = len(self.pipes[0])
        self.s = self.find_s()
        self.loop = self.find_loop()

    def find_s(self) -> tuple[int, int]:
        for iy in range(len(self.pipes)):
            jx = self.pipes[iy].find('S')
            if jx >= 0:
                return iy, jx
        return -1, -1

    def find_s_directions(self) -> list[Side]:
        return [side for side in SHIFT if PIPES[self.pipes[self.s[0] + SHIFT[side][0]][self.s[1] + SHIFT[side][1]]] & NEIGHBOURS[side]]

    def find_loop(self) -> list[tuple[int, int]]:
        loop: list[tuple[int, int]] = []
        iy, jx = self.s
        dd = self.find_s_directions()
        if len(dd) != 2:
            raise 'UNEXPECTED DIRECTIONS NUMBER'
        PIPES['S'] = sum(dd)
        came_from = dd.pop()
        while not len(loop) or (iy, jx) != self.s:
            loop.append((iy, jx))
            go_to = PIPES[self.pipes[iy][jx]] - came_from
            iy += SHIFT[go_to][0]
            jx += SHIFT[go_to][1]
            came_from = NEIGHBOURS[go_to]
        return loop


class SolveDay10x2(SolveDay10x1):
    def solve(self, text_input: str) -> int:
        self.parse_input(text_input)
        if self.verbose:
            print(sorted(self.loop))
        loop_items = {}
        rows: list[list[int]] = []

        for _ in range(self.height):
            rows.append([])

        for iy, jx in sorted(self.loop):
            pipe = PIPES[self.pipes[iy][jx]]
            loop_items[(iy, jx)] = pipe
            if pipe & Side.N:
                rows[iy].append(jx)
        if self.verbose:
            print(rows)

        surrounded: list[tuple[int, int]] = []

        for iy in range(self.height):
            for jx in range(self.width):
                if (iy, jx) in loop_items:
                    continue
                crosses = sum(1 for z in rows[iy] if z < jx)
                if crosses % 2:
                    surrounded.append((iy, jx))
        if self.verbose:
            print('surrounded =',surrounded)
        return len(surrounded)
