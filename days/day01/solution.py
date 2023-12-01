from days import SolveDay


class SolveDay01x1(SolveDay):
    NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def solve(self, text_input: str) -> int:
        return sum(self.get_line_value(x) for x in self.get_lines(text_input))

    def get_line_value(self, line: str) -> int:
        return int(self.find_number(line) + self.find_number(line, True))

    def find_number(self, line: str, backwards=False) -> str:
        step = backwards and -1 or 1

        ix = backwards and -1 or 0

        for _ in range(len(line)):
            c = line[ix]
            if c in self.NUMBERS:
                return str(c)
            ix += step

        return '0'


class SolveDay01x2(SolveDay01x1):
    def find_number(self, line: str, backwards=False) -> str:
        return '0'
