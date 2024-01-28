from days import SolveDay

Point = tuple[int, int]


class ReachedTiles:
    def __init__(self):
        self.all: set[Point] = set()
        self.front: set[Point] = set()

    def add(self, point: Point):
        if point not in self.all:
            self.all.add(point)
            self.front.add(point)

    def print(self):
        print(self.all, '|', self.front)


class Reached:
    current_ix: int

    def __init__(self, starting_point: Point):
        self.current_ix = 0
        self.even = ReachedTiles()
        self.odd = ReachedTiles()

    def complete(self):
        self.get_current().front = set()
        self.current_ix = 1 - self.current_ix

    def get_current(self) -> ReachedTiles:
        return self.current_ix and self.odd or self.even

    def get_next(self) -> ReachedTiles:
        return self.current_ix and self.even or self.odd


class SolveDay21x1(SolveDay):
    lines: list[str]
    size: 0
    reached: Reached

    def solve(self, text_input: str, steps=64) -> int:
        self.init_problem(text_input)
        if self.verbose:
            self.reached.get_current().print()
        for step in range(steps):
            if self.verbose:
                print('STEP', step + 1)
            self.go()

        return len(self.reached.get_current().all)

    def init_problem(self, text_input: str):
        self.lines = self.get_lines(text_input)
        self.size = len(self.lines)
        m = self.size // 2
        self.reached = Reached((m, m))
        self.reached.get_current().add((m, m))

    def go(self):
        for x in self.reached.get_current().front:
            for y in self.find_ways(x):
                self.reached.get_next().add(y)
        self.reached.complete()
        if self.verbose:
            self.reached.get_current().print()

    def find_ways(self, point: Point) -> list[Point]:
        ix, jy = point
        neighbours = ((ix - 1, jy), (ix + 1, jy), (ix, jy - 1), (ix, jy + 1))
        return [x for x in neighbours if self.is_garden_plot(x)]

    def is_garden_plot(self, point: Point) -> bool:
        ix, jy = point
        return 0 <= ix < self.size and 0 <= jy < self.size and self.lines[ix][jy] == '.'


class SolveDay21x2(SolveDay21x1):
    def is_garden_plot(self, point: Point) -> bool:
        ix, jy = point
        ix = ix % self.size
        jy = jy % self.size
        return self.lines[ix][jy] in '.S'
