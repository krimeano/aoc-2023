from days import SolveDay


class SolveDay01x1(SolveDay):
    NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solve(self, text_input: str) -> int:
        return sum(self.get_line_value(x) for x in self.get_lines(text_input))

    def get_line_value(self, line: str) -> int:
        r = self.find_number(line) + self.find_number(line, True)
        return int(r)

    def find_number(self, line: str, backwards=False) -> str:
        step = backwards and -1 or 1

        ix = backwards and -1 or 0

        for _ in range(len(line)):
            c = line[ix]
            if c in self.NUMBERS:
                return str(c)
            ix += step

        return ''


class SolveDay01x2(SolveDay01x1):
    NAMES = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    SUBS = {}
    BB = {}
    EE = {}

    def __init__(self, verbose=False):
        super().__init__(verbose)

        for ix in range(len(self.NAMES)):
            name = self.NAMES[ix]
            value = str(ix + 1)
            self.SUBS[name] = value

            first, last = name[0], name[-1]

            if first not in self.BB:
                self.BB[first] = []

            self.BB[first].append(name)

            if last not in self.EE:
                self.EE[last] = []

            self.EE[last].append(name)

    def find_number(self, line: str, backwards=False) -> str:
        step = backwards and -1 or 1

        ix = backwards and -1 or 0
        cc = backwards and self.EE or self.BB

        size = len(line)
        for _ in range(size):
            c = line[ix]
            if c in self.NUMBERS:
                return str(c)
            if c in cc:
                for name in cc[c]:
                    jy = ix + step * len(name)
                    m, n = ix > jy and (size + jy + 1, size + ix + 1) or (ix, jy)
                    if line[m:n] == name:
                        return self.SUBS[name]
            ix += step

        return ''
