from days import SolveDay


def sign(number: float):
    if number < 0:
        return -1
    if number > 0:
        return 1
    return 0


def ab_cross_cd(ab: tuple[float, float], cd: tuple[float, float]) -> float:
    result = ab[0] * cd[1] - ab[1] * cd[0]
    if not result:
        print(ab, cd)
        raise BaseException('COLLINEAR!')
    return result


def abc_cross(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> float:
    return ab_cross_cd((b[0] - a[0], b[1] - a[1]), (c[0] - a[0], c[1] - a[1]))


class HailStone:
    def __init__(self, init_str: str, radius: int, origin=0, verbose=False):
        self.verbose = verbose
        self.radius = radius
        [self.start, self.speed] = [tuple(int(y) for y in x.split(', ')) for x in init_str.split(' @ ')]
        self.start = tuple(x - origin for x in self.start)
        self.fixed = ab_cross_cd((self.start[0], self.start[1]), (self.speed[0], self.speed[1]))

    def __str__(self):
        a = '[{0}, {1}]@({2}, {3})'.format(self.start[0], self.start[1], self.speed[0], self.speed[1])
        return a

    def calculate_crossing_time(self, ix: int, factor=1) -> float:
        return (factor * sign(self.speed[ix]) * self.radius - self.start[ix]) / self.speed[ix]

    def calculate_coords(self, t: float) -> tuple[float, float]:
        return self.calculate_coord(0, t), self.calculate_coord(1, t)

    def calculate_coord(self, ix: int, t: float) -> float:
        return self.start[ix] + t * self.speed[ix]

    def test_crossing(self, other) -> bool:
        if self.verbose:
            print('A ', self)
            print('B ', other)

        if self.parallel_xy_projection(other):
            if self.verbose:
                print('PARALLEL. never cross')
            return False

        result = True
        crossing = self.find_crossing(other)
        if self.verbose:
            print('Cross at', crossing, end='')
        if not self.test_coords(crossing):
            if self.verbose:
                print(' outside the box', end='')
            result = False
        elif self.verbose:
            print(' inside the box', end='')

        in_the_past = False
        if not self.test_time(crossing):
            in_the_past = True
            if self.verbose:
                print(' in the past for A', end='')

        if not other.test_time(crossing):
            if self.verbose:
                print(' in the past for B', end='')
            in_the_past = True
        if in_the_past:
            if self.verbose:
                print()
            result = False
        elif self.verbose:
            print(' in the future')

        if self.verbose:
            print(result)

        return result

    def parallel_xy_projection(self, other) -> bool:
        return self.speed[0] * other.speed[1] == self.speed[1] * other.speed[0]

    def find_crossing(self, other) -> tuple[float, float]:
        s = ab_cross_cd((self.speed[0], self.speed[1]), (other.speed[0], other.speed[1]))
        x = (other.fixed * self.speed[0] - self.fixed * other.speed[0]) / s
        y = (other.fixed * self.speed[1] - self.fixed * other.speed[1]) / s
        return x, y

    def test_coords(self, crossing: tuple[float, float]) -> bool:
        return -self.radius <= crossing[0] <= self.radius and -self.radius <= crossing[1] <= self.radius

    def test_time(self, crossing: tuple[float, float]) -> bool:
        return self.validate_time_ort(crossing, 0) and self.validate_time_ort(crossing, 1)

    def validate_time_ort(self, crossing: tuple[float, float], ix: int) -> bool:
        return crossing[ix] == self.start[ix] or sign(self.speed[ix]) == sign(crossing[ix] - self.start[ix])


class SolveDay24x1(SolveDay):
    def solve(self, text_input: str, radius=1 * 10 ** 14, origin=3 * 10 ** 14) -> int:
        hail_stones = []
        for line in self.get_lines(text_input):
            hail_stone = HailStone(line, radius, origin, self.verbose)
            if self.verbose:
                print(hail_stone)
            hail_stones.append(hail_stone)

        total = 0
        for ix in range(len(hail_stones) - 1):
            for jy in range(ix + 1, len(hail_stones)):
                if self.verbose:
                    print()
                total += hail_stones[ix].test_crossing(hail_stones[jy])

        return total


class SolveDay24x2(SolveDay24x1):
    def solve(self, text_input: str, radius=1 * 10 ** 14, origin=3 * 10 ** 14) -> int:
        return 0
