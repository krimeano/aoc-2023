from days import SolveDay


def sign(number: float):
    if number < 0:
        return -1
    if number > 0:
        return 1
    return 0


class HailStone:
    def __init__(self, init_str: str, radius: int, origin=0):
        [self.xyz, self.vvv] = [tuple(int(y) for y in x.split(', ')) for x in init_str.split(' @ ')]
        self.radius = radius
        self.xyz = tuple(x - origin for x in self.xyz)
        self.enters = self.calculate_enters()
        self.leaves = self.calculate_leaves()

    def __str__(self):
        a = '[{0}, {1}]@({2}, {3})'.format(self.xyz[0], self.xyz[1], self.vvv[0], self.vvv[1])
        b = '[{0}, {1}]>[{2}, {3}]'.format(self.enters[0], self.enters[1], self.leaves[0], self.leaves[1])
        return a + ': ' + b

    def calculate_enters(self) -> tuple[float, float]:
        t = max(0, *[self.calculate_crossing_time(ix, -1) for ix in range(2)])
        return self.calculate_coords(t)

    def calculate_leaves(self) -> tuple[float, float]:
        t = min(*[self.calculate_crossing_time(ix) for ix in range(2)])
        return self.calculate_coords(t)

    def calculate_crossing_time(self, ix: int, factor=1) -> float:
        return (factor * sign(self.vvv[ix]) * self.radius - self.xyz[ix]) / self.vvv[ix]

    def calculate_coords(self, t: float) -> tuple[float, float]:
        return self.calculate_coord(0, t), self.calculate_coord(1, t)

    def calculate_coord(self, ix: int, t: float) -> float:
        return self.xyz[ix] + t * self.vvv[ix]


def ab_cross_cd(ab: tuple[float, float], cd: tuple[float, float]) -> float:
    result = ab[0] * cd[1] - ab[1] * cd[0]
    if not result:
        raise 'COLLINEAR!'
    return result


def abc_cross(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> float:
    return ab_cross_cd((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))


def get_orientations(ab: HailStone, cd: HailStone) -> tuple[float, float]:
    return abc_cross(ab.enters, ab.leaves, cd.enters), abc_cross(ab.enters, ab.leaves, cd.leaves)


def test_crossing(a: HailStone, b: HailStone, verbose: bool) -> bool:
    if verbose:
        print('A ', a)
        print('B ', b)
    ab = get_orientations(a, b)
    ba = get_orientations(b, a)
    result = sign(ab[0]) != sign(ab[1]) and sign(ba[0]) != sign(ba[1])
    if verbose:
        print(ab, ba, result)
    return result


class SolveDay24x1(SolveDay):
    def solve(self, text_input: str, radius=1 * 10 ** 14, origin=3 * 10 ** 14) -> int:
        hail_stones = []
        for line in self.get_lines(text_input):
            hail_stone = HailStone(line, radius, origin)
            if self.verbose:
                print(hail_stone)
            hail_stones.append(hail_stone)

        total = 0
        for ix in range(len(hail_stones) - 1):
            for jy in range(ix + 1, len(hail_stones)):
                if self.verbose:
                    print()
                total += test_crossing(hail_stones[ix], hail_stones[jy], self.verbose)

        return total


class SolveDay24x2(SolveDay24x1):
    def solve(self, text_input: str, radius=1 * 10 ** 14, origin=3 * 10 ** 14) -> int:
        return 0
