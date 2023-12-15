from days import SolveDay


class SolveDay14x1(SolveDay):
    rocks: list[tuple[int, int]]
    height: int

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input)
        if self.verbose:
            print(self.height, self.rocks)
        # progression sum = (first + last) * items;
        # first - last = items - 1
        # last = first - items + 1
        # first = height - index
        # last = height - index - items + 1
        # progression sum = height - index + height - index - items + 1
        return sum([(2 * self.height - 2 * rock - rolls + 1) * rolls for (rock, rolls) in self.rocks]) // 2

    def parse_input(self, text_input):
        self.rocks = []
        lines = self.get_lines(text_input)
        self.height = len(lines)
        width = self.height and len(lines[0])

        for ix in range(width):
            current_rock_index = 0
            rolls = 0
            for jy in range(self.height):
                r = lines[jy][ix]
                if r == 'O':
                    rolls += 1
                    continue
                if r == '#':
                    if rolls:
                        self.rocks.append((current_rock_index, rolls))
                    current_rock_index = jy + 1
                    rolls = 0
            else:
                if rolls:
                    self.rocks.append((current_rock_index, rolls))


class SolveDay14x1x2(SolveDay):
    size: int
    rocks: list[list[int]]
    rolls: list[list[int]]

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input)
        self.tilt()
        return self.count()

    def count(self):
        return sum([self.size * len(x) - sum(x) for x in self.rolls])

    def parse_input(self, text_input):
        lines = self.get_lines(text_input)
        self.size = len(lines)
        self.rocks = []
        self.rolls = []

        for ix in range(self.size):
            col_rocks = []
            col_rolls = []
            for jy in range(self.size):
                r = lines[jy][ix]
                if r == '#':
                    col_rocks.append(jy)
                if r == 'O':
                    col_rolls.append(jy)
            self.rocks.append(col_rocks)
            self.rolls.append(col_rolls)
        if self.verbose:
            print('init:')
            print(self.rocks)
            print(self.rolls)

    def tilt(self):
        for ix in range(self.size):
            rocks = self.rocks[ix] + [self.size]
            rolls = self.rolls[ix]
            last_roll = -1
            jy = 0
            for next_rock in rocks:
                while jy < len(rolls):
                    if rolls[jy] > next_rock:
                        last_roll = next_rock
                        break
                    last_roll += 1
                    rolls[jy] = last_roll
                    jy += 1
        return self


class SolveDay14x2(SolveDay14x1x2):
    cycles: int

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input)
        self.cycles = 0
        total_cycles = 1000000000
        position = str(self)
        position_per_cycle = [position]
        values_per_cycle = [self.count()]
        position_met = {position: 0}
        started_at = 0
        period = 0
        for _ in range(total_cycles):
            self.cycle()
            position = str(self)
            position_per_cycle.append(position)
            values_per_cycle.append(self.count())
            if position in position_met:
                started_at = position_met[position]
                period = self.cycles - started_at
                if self.verbose:
                    print('ALREADY MET AFTER CYCLE', position_met[position], 'CURRENT CYCLE:', self.cycles)
                break
            position_met[position] = self.cycles
        ix = (total_cycles - started_at) % period
        if self.verbose:
            print(started_at, period, ix, values_per_cycle)
        return values_per_cycle[started_at + ix]

    def cycle(self):
        self.cycles += 1
        self.tilt().turn().tilt().turn().tilt().turn().tilt().turn()
        if self.verbose:
            print('after cycle {0}:'.format(self.cycles), self.count(), str(self))

    def turn(self):
        self.rocks = turn_items(self.rocks)
        self.rolls = turn_items(self.rolls)
        return self

    def __str__(self):
        return ';'.join([','.join([str(x) for x in xx]) for xx in self.rolls])


def turn_items(items: list[list[int]]) -> list[list[int]]:
    out = []
    size = len(items)
    for _ in range(size):
        out.append([])
    for ix in range(size):
        for jy in items[ix]:
            out[size - 1 - jy].append(ix)
    return out
