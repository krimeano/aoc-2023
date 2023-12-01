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
    # bb: efnost
    # ee: enortx
    # cc: enot
    SUBS = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': '4',
        'five': '5e',
        'six': '6',
        'seven': '7n',
        'eight': 'e8t',
        'nine': 'n9e',
    }

    def find_number(self, line: str, backwards=False) -> str:
        return super().find_number(self.preprocess_line(line), backwards)

    def preprocess_line(self, line: str) -> str:
        out = line
        for x in self.SUBS:
            out = self.SUBS[x].join(out.split(x))
        return out
