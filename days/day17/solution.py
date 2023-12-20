from days import SolveDay
from .block import Block, ORTS


class SolveDay17x1(SolveDay):
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


class SolveDay17x2(SolveDay17x1):

    def solve(self, text_input: str) -> int:
        return 0
