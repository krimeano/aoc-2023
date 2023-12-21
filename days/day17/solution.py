from days import SolveDay
from .block import Block, ORTS


class SolveDay17x1Alpha(SolveDay):
    size: int
    blocks: list[list[Block]]

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input).go()
        last = self.blocks[-1][-1]
        if self.verbose:
            print('LAST:', last)
        return min([last.enters[x] for x in last.enters])

    def parse_input(self, text_input: str):
        lines = self.get_lines(text_input)
        self.size = len(lines)
        self.blocks = []
        for jy in range(self.size):
            row = []
            for ix in range(self.size):
                row.append(Block(jy, ix, int(lines[jy][ix])))
            self.blocks.append(row)
        return self

    def go(self):

        improved_blocks = {self.blocks[0][0]}
        while len(improved_blocks):
            block = improved_blocks.pop()
            if self.verbose:
                print('current block is', block)
            for ort in ORTS:
                iy = block.iy + ort[0]
                jx = block.jx + ort[1]
                if 0 <= iy < self.size and 0 <= jx < self.size:
                    neighbour = self.blocks[iy][jx]
                    if self.verbose:
                        print('\timproving', neighbour)
                    was_improved = neighbour.improve(block)
                    if was_improved:
                        improved_blocks.add(neighbour)
                        if self.verbose:
                            print('\t\timproved', neighbour)
            if self.verbose:
                print('\tconsidering blocks:', len(improved_blocks))


YX = tuple[int, int]
HM = list[list[int]]


class SolveDay17x1(SolveDay):
    limits = (0, 3)
    size: int
    heat_loss_map: HM
    h2v: HM
    v2h: HM

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input).go()
        return min([self.h2v[-1][-1], self.v2h[-1][-1]])

    def parse_input(self, text_input: str):
        self.heat_loss_map = [[int(x) for x in line] for line in self.get_lines(text_input)]
        self.size = len(self.heat_loss_map)
        m = (3 * self.size) ** 2
        self.h2v = [[m] * self.size for _ in range(self.size)]
        self.v2h = [[m] * self.size for _ in range(self.size)]
        self.v2h[0][0] = 0
        self.h2v[0][0] = 0
        self.print()
        return self

    def go(self):
        is_vertical = True
        blocks_to_visit: set[YX] = {(0, 0)}
        improved_blocks: set[YX] = {(0, 0)}

        while blocks_to_visit:
            current_map = is_vertical and self.h2v or self.v2h
            perpendicular_map = is_vertical and self.v2h or self.h2v
            y0x0 = blocks_to_visit.pop()
            leaving_value = current_map[y0x0[0]][y0x0[1]]
            negative_step = is_vertical and (-1, 0) or (0, -1)
            positive_step = is_vertical and (1, 0) or (0, 1)
            improved_blocks = self.move(leaving_value, y0x0, negative_step, perpendicular_map, improved_blocks)
            improved_blocks = self.move(leaving_value, y0x0, positive_step, perpendicular_map, improved_blocks)

            if not blocks_to_visit:
                if self.verbose:
                    print(improved_blocks)
                is_vertical = not is_vertical
                blocks_to_visit = improved_blocks
                improved_blocks = set()
        self.print()

    def move(self, value: int, y0x0: YX, step: YX, values: HM, improved_blocks: set[YX]) -> set[YX]:
        y, x = y0x0
        dy, dx = step
        for kz in range(self.limits[1]):
            y += dy
            x += dx

            if not (0 <= y < self.size and 0 <= x < self.size):
                break

            value += self.heat_loss_map[y][x]

            if not self.limits[0] <= kz < self.limits[1]:
                continue

            old_value = values[y][x]

            if value < old_value:
                values[y][x] = value
                improved_blocks.add((y, x))
                if self.verbose:
                    print('improved', self.str_item(y, x))

        return improved_blocks

    def print(self):
        if not self.verbose:
            return

        for iy in range(self.size):
            for jx in range(self.size):
                print(self.str_item(iy, jx), end=' ')
            print()

    def str_item(self, iy, jx):
        x = self.heat_loss_map[iy][jx]
        y = self.h2v[iy][jx]
        z = self.v2h[iy][jx]
        return '{0}|{1}-{2}'.format(x, y, z)


class SolveDay17x2(SolveDay17x1):
    limits = (3, 10)
