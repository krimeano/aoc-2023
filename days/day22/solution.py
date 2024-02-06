from days import SolveDay


def parse_coords(txt: str) -> list[int]:
    return [int(x.strip()) for x in txt.split(',')]


class Brick:
    counter = 0

    def __init__(self, txt: str):
        self.ix = Brick.counter
        self.supporting = set()
        self.supported_by = set()
        self.moved = False
        Brick.counter += 1
        edges = [parse_coords(x) for x in txt.split('~')]
        dd = [edges[1][ix] - edges[0][ix] for ix in range(len(edges[0]))]
        self.position = edges[0]
        self.direction = dd[0], dd[1], dd[2]

    def spur(self) -> list[tuple[int, int]]:
        if not self.direction[0] and not self.direction[1]:
            return [(self.position[0], self.position[1])]
        x0 = self.position[0]
        y0 = self.position[1]
        out = []
        for dx in range(self.direction[0] + 1):
            for dy in range(self.direction[1] + 1):
                out.append((x0 + dx, y0 + dy))
        return out

    def support_me(self, other):
        self.supporting.add(other.ix)
        other.supported_by.add(self.ix)

    def __str__(self):
        aa = self.position
        bb = [self.position[ix] + self.direction[ix] for ix in range(len(self.direction))]
        return '~'.join([','.join([str(a) for a in aa]), ','.join([str(b) for b in bb])])

    def debug(self):
        print('#' + str(self.ix), str(self), self.position, self.direction, self.spur(), self.position[2])

    def __gt__(self, other) -> bool:
        return self.position[::-1] > other.position[::-1]

    def __lt__(self, other):
        return self.position[::-1] < other.position[::-1]

    def __eq__(self, other):
        return self.position == other.position


class SolveDay22x1(SolveDay):
    bricks: dict[int, Brick]
    bottom: dict[tuple[int, int], tuple[int, int]]  # {(x, y): (z, brick.ix)}

    def solve(self, text_input: str) -> int:
        self.handle_snapshot(self.get_lines(text_input))
        result = 0
        for ix in self.bricks:
            brick = self.bricks[ix]
            if self.verbose:
                brick.debug()
            can_be_removed = self.can_be_removed(brick)
            if self.verbose:
                print('   ', brick.supporting, brick.supported_by, can_be_removed)
            if can_be_removed:
                result += 1

        return result

    def handle_snapshot(self, snapshot: list[str]):
        self.bottom = {}
        self.bricks = {}
        Brick.counter = 0
        for brick in sorted(Brick(x) for x in snapshot):
            self.bricks[brick.ix] = brick
            if self.verbose:
                brick.debug()
            heights: dict[int, list[tuple[int, int]]] = {}
            h_max = 0
            for xy in brick.spur():
                if xy not in self.bottom:
                    self.bottom[xy] = (0, -1)

                h = self.bottom[xy][0]

                if h < h_max:
                    continue

                if h > h_max:
                    heights = {}
                    h_max = h

                if h not in heights:
                    heights[h] = []
                heights[h].append(xy)

            if self.verbose:
                print('   ', heights)

            for xy in heights[h_max]:
                ix = self.bottom[xy][1]
                if ix >= 0:
                    self.bricks[ix].support_me(brick)

            z0 = h_max + 1
            brick.position[2] = z0
            for xy in brick.spur():
                z = z0
                if brick.direction[2] > 0:
                    z += brick.direction[2]
                self.bottom[xy] = (z, brick.ix)

            if self.verbose:
                brick.debug()
                print()
        if self.verbose:
            print(self.bottom)

    def can_be_removed(self, brick):
        for ix in brick.supporting:
            other = self.bricks[ix]
            if len(other.supported_by) < 2:
                return False
        return True


class SolveDay22x2(SolveDay22x1):
    def solve(self, text_input: str) -> int:
        self.handle_snapshot(self.get_lines(text_input))
        return sum(self.move(self.bricks[ix]) for ix in self.bricks)

    def move(self, start: Brick) -> int:
        for ix in self.bricks:
            self.bricks[ix].moved = False

        start.moved = True

        just_moved = [start]
        while just_moved:
            current = just_moved.pop()

            for ix in current.supporting:
                other = self.bricks[ix]

                for jy in other.supported_by:
                    if not self.bricks[jy].moved:
                        break
                else:
                    other.moved = True
                    just_moved.append(other)

        return sum(1 for ix in self.bricks if self.bricks[ix].moved) - 1
