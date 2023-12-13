from days import SolveDay
from .pattern import Pattern, PatternSmudged


class SolveDay13x1(SolveDay):
    ignore_empty_lines = False
    patterns: list[Pattern]

    def solve(self, text_input: str) -> int:
        self.parse_patterns(self.get_lines(text_input))

        if self.verbose:
            for pattern in self.patterns:
                print('-' * 70)
                print(pattern)

        return sum(int(pattern) for pattern in self.patterns)

    def parse_patterns(self, lines: list[str]):
        self.patterns = []
        current_pattern = []
        for line in lines:
            if not line:
                if current_pattern:
                    self.patterns.append(self.init_pattern(current_pattern))
                current_pattern = []
            else:
                current_pattern.append(line)
        if current_pattern:
            self.patterns.append(self.init_pattern(current_pattern))

    def init_pattern(self, str_pattern: list[str]):
        pattern = Pattern(str_pattern, self.verbose)
        pattern.get_mirrors()
        return pattern


class SolveDay13x2(SolveDay13x1):
    def init_pattern(self, str_pattern: list[str]):
        pattern = PatternSmudged(str_pattern, self.verbose)
        pattern.get_mirrors()
        return pattern
