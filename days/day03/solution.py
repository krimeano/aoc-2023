from days import SolveDay

NUMBERS = '1234567890'


class SolveDay03x1(SolveDay):
    part_numbers: list[int] = []
    not_part_numbers: list[int] = []
    lines: list[str] = []
    width = 0
    height = 0

    def solve(self, text_input: str) -> int:
        self.set_initial(text_input)
        self.part_numbers, self.not_part_numbers = [], []
        self.find_numbers()
        if self.verbose:
            print('not_part_numbers', self.not_part_numbers)
            print('part_numbers', self.part_numbers)
        return sum(self.part_numbers)

    def set_initial(self, text_input: str):
        if self.verbose:
            print('\n' + '-' * 79 + '\n')
        self.lines = self.get_lines(text_input)
        self.height = len(self.lines)
        self.width = self.height and len(self.lines[0]) or 0

    def find_numbers(self) -> None:
        for pos in self.find_number_positions():
            number = int(self.lines[pos[0]][pos[1][0]:pos[1][1]])
            around = self.get_indexes_around(pos)

            if self.verbose:
                print(pos, number, around)

            for iy, jx in around:
                c = self.lines[iy][jx]
                if c != '.':
                    self.part_numbers.append(number)
                    break
            else:
                self.not_part_numbers.append(number)

    def find_number_positions(self) -> list[tuple[int, tuple[int, int]]]:
        out = []
        for iy in range(self.height):
            out += [[iy, xx] for xx in self.find_number_positions_per_line(self.lines[iy])]
        return out

    def find_number_positions_per_line(self, line: str) -> list[tuple[int, int]]:
        size = len(line)

        if size != self.width:
            raise 'Width of line "%s" is different!' % line

        out = []
        looking_end_of_number = False
        x0 = 0
        jx = 0
        while jx <= size:
            if jx < size and line[jx] in NUMBERS:
                if not looking_end_of_number:
                    looking_end_of_number = True
                    x0 = jx
            else:
                if looking_end_of_number:
                    looking_end_of_number = False
                    out.append((x0, jx))

            jx += 1

        return out

    def get_indexes_around(self, pos: tuple[int, tuple[int, int]]) -> list[tuple[int, int]]:
        out = []
        y, (x0, x1) = pos

        if x0 > 0:
            out.append((y, x0 - 1))

        if x1 < self.width:
            out.append((y, x1))

        jj = []
        if y > 0:
            jj.append(y - 1)
        if y + 1 < self.height:
            jj.append(y + 1)

        for iy in jj:
            for jx in range(max([0, x0 - 1]), min([x1 + 1, self.width])):
                out.append((iy, jx))
        return out


class SolveDay03x2(SolveDay03x1):
    asterisks = dict()

    def solve(self, text_input: str) -> int:
        self.set_initial(text_input)
        self.asterisks = dict()
        self.find_asterisks()
        if self.verbose:
            print('asterisks', self.asterisks)

        return sum([self.asterisks[xy][0] * self.asterisks[xy][1] for xy in self.asterisks if len(self.asterisks[xy]) > 1])

    def find_asterisks(self) -> None:
        for pos in self.find_number_positions():
            number = int(self.lines[pos[0]][pos[1][0]:pos[1][1]])
            around = self.get_indexes_around(pos)

            if self.verbose:
                print(pos, number, around)

            for iy, jx in around:
                c = self.lines[iy][jx]
                if c == '*':
                    if (iy, jx) not in self.asterisks:
                        self.asterisks[(iy, jx)] = []
                    self.asterisks[(iy, jx)].append(number)
