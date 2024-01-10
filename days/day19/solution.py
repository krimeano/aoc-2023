from days import SolveDay

Rule = tuple[str, str, int, str] | tuple[str, str]


class SolveDay19x1(SolveDay):
    workflows: dict[str, list[Rule]]
    parts: list[dict[str, int]]

    def solve(self, text_input: str) -> int:
        valid_parts = self.parse_input(text_input).get_valid_parts()
        return sum(sum(part[x] for x in part) for part in valid_parts)

    def parse_input(self, text_input: str):
        self.workflows = {}
        self.parts = []
        for line in self.get_lines(text_input):
            self.parse_line(line)
        return self

    def get_valid_parts(self):
        return [x for x in self.parts if self.validate_part(x)]

    def parse_line(self, line: str):
        if not line:
            return
        if line.startswith('{'):
            self.parse_part(line)
            return
        self.parse_workflow(line)

    def parse_workflow(self, line: str):
        parts = line[:-1].split('{')
        name = parts[0]
        rules = []
        for r in parts[1].split(','):
            xx = r.split(':')
            if len(xx) == 1:
                rules.append(('*', r))
            else:
                rules.append((xx[0][1], xx[0][0], int(xx[0][2:]), xx[1]))
        if self.verbose:
            print('parsed workflow', name, rules)
        self.workflows[name] = rules

    def parse_part(self, line: str):
        part = {y[0]: int(y[1]) for y in [x.split('=') for x in line[1:-1].split(',')]}
        if self.verbose:
            print('parsed part', part)
        self.parts.append(part)

    def validate_part(self, part: dict[str, int]) -> bool:
        current_name = 'in'
        visited = {'A', 'R'}
        while current_name not in visited:
            visited.add(current_name)
            for rule in self.workflows[current_name]:
                if rule[0] == '*':
                    current_name = rule[-1]
                    break
                else:
                    a = part[rule[1]]
                    b = rule[2]
                    if (rule[0] == '>' and a > b) or (rule[0] == '<' and a < b):
                        current_name = rule[-1]
                        break
        is_valid = current_name == 'A'
        if self.verbose:
            print('is valid', is_valid, part)
        return is_valid


class SolveDay19x2(SolveDay19x1):

    def solve(self, text_input: str) -> int:
        return 0
