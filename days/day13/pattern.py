class Pattern:

    def __init__(self, lines: list[str], verbose=False):
        self.verbose = verbose
        self.lines = lines
        self.height = len(lines)
        self.width = self.height and len(lines[0])
        self.mirror_horizontal = 0
        self.mirror_vertical = 0

        self.rows: list[int] = [0] * self.height
        self.cols: list[int] = [0] * self.width

        for iy in range(self.height):
            for jx in range(self.width):
                self.rows[iy] <<= 1
                self.cols[jx] <<= 1
                if self.lines[iy][jx] == '#':
                    self.rows[iy] += 1
                    self.cols[jx] += 1

    def __str__(self):
        return '\n'.join(
            ['{0} {1:>10}'.format(self.lines[iy], self.rows[iy]) for iy in range(self.height)]
            + [
                ' '.join([str(x) for x in self.cols]),
                'h = {0}, v = {1}'.format(self.mirror_horizontal, self.mirror_vertical)
            ]
        )

    def __int__(self):
        return self.mirror_horizontal * 100 + self.mirror_vertical

    def get_mirrors(self) -> tuple[int, int]:
        self.mirror_horizontal = self.find_mirrors(self.rows)
        self.mirror_vertical = self.find_mirrors(self.cols)
        return self.mirror_horizontal, self.mirror_vertical

    def find_mirrors(self, xx: list[int]) -> int:
        for ix in self.find_possible_mirrors(xx):
            if self.test_is_mirror(xx, ix):
                if self.verbose:
                    print('mirror found at', ix)
                return ix
        return 0

    def find_possible_mirrors(self, xx: list[int]) -> list[int]:
        possible = [ix for ix in range(1, len(xx)) if xx[ix - 1] == xx[ix]]
        if self.verbose:
            print('possible mirrors:', xx, possible)
        return possible

    def test_is_mirror(self, xx: list[int], mirror_at: int) -> bool:
        shortest = min(mirror_at, len(xx) - mirror_at)
        for ix in range(1, shortest):
            if xx[mirror_at - 1 - ix] != xx[mirror_at + ix]:
                return False
        return True


class PatternSmudged(Pattern):
    def __init__(self, lines: list[str], verbose=False):
        super().__init__(lines, verbose)
        self.smudges = set([2 ** ix for ix in range(max(self.height, self.width))])
        if self.verbose:
            print(self.smudges)

    def find_possible_mirrors(self, xx: list[int]) -> list[int]:
        possible = [(ix, abs(xx[ix - 1] - xx[ix])) for ix in range(1, len(xx)) if (xx[ix - 1] ^ xx[ix]) in self.smudges or xx[ix - 1] == xx[ix]]
        if self.verbose:
            print('possible mirrors:', xx, possible)
        return [x[0] for x in possible]

    def test_is_mirror(self, xx: list[int], mirror_at: int) -> bool:
        smudges_found = 0
        shortest = min(mirror_at, len(xx) - mirror_at)
        for ix in range(shortest):
            diff = abs(xx[mirror_at + ix] - xx[mirror_at - 1 - ix])

            if diff:
                if diff in self.smudges:
                    smudges_found += 1
                    if smudges_found > 1:
                        return False
                else:
                    return False

        return smudges_found == 1
