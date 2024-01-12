from days import SolveDay

Rule = tuple[str, str, int, str] | tuple[str, str]


class SolveDay19x1(SolveDay):
    workflows: dict[str, list[Rule]]
    parts: list[dict[str, int]]

    def solve(self, text_input: str) -> int:
        valid_parts = self.parse_input(text_input).optimize_workflows().get_valid_parts()
        return sum(sum(part[x] for x in part) for part in valid_parts)

    def parse_input(self, text_input: str):
        self.workflows = {}
        self.parts = []
        for line in self.get_lines(text_input):
            self.parse_line(line)
        return self

    def optimize_workflows(self):
        ww = self.sort_workflows()[::-1]
        aliases = {}
        for name in ww:
            rules = self.workflows[name]
            prev = ''
            for rule in rules:
                cur = rule[-1]
                cur = cur in aliases and aliases[cur] or cur
                if prev and prev != cur:
                    break
                prev = cur
            else:
                self.workflows[name] = rules[-1:]
                aliases[name] = prev
            new_rules = []
            for rule in self.workflows[name]:
                if rule[-1] in aliases:
                    fixed = aliases[rule[-1]]
                    if len(rule) == 2:
                        new_rules.append((rule[0], fixed))
                    else:
                        new_rules.append((rule[0], rule[1], rule[2], fixed))
                else:
                    new_rules.append(rule)
            self.workflows[name] = new_rules

        for name in aliases:
            del self.workflows[name]

        if self.verbose:
            for name in self.sort_workflows():
                print('optimized', name, self.workflows[name])
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
                cmp = xx[0][1]
                value = int(xx[0][2:])
                if cmp == '>':
                    cmp = '>='
                    value += 1
                rules.append((cmp, xx[0][0], value, xx[1]))
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
                    if (rule[0] == '>=' and a >= b) or (rule[0] == '<' and a < b):
                        current_name = rule[-1]
                        break
        is_valid = current_name == 'A'
        if self.verbose:
            print('is valid', is_valid, part)
        return is_valid

    def sort_workflows(self) -> list[str]:
        references: dict[str, int] = {}
        for name in self.workflows:
            for rule in self.workflows[name]:
                x = rule[-1]
                if x in 'AR':
                    continue
                if x not in references:
                    references[x] = 0
                references[x] += 1
        if self.verbose:
            print(references)
        data = ['in']
        out = []
        while data:
            current_name = data.pop(0)
            out.append(current_name)
            for rule in self.workflows[current_name]:
                x = rule[-1]
                if x in 'AR':
                    continue
                references[x] -= 1
                if not references[x]:
                    data.append(x)
        if self.verbose:
            print(out)
        return out


class SolveDay19x2(SolveDay19x1):
    points: dict[str, list[int]]

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input).optimize_workflows().mark_axes()
        return self.calculate()

    def parse_line(self, line: str):
        if line and not line.startswith('{'):
            self.parse_workflow(line)

    def mark_axes(self):
        self.points = {
            'x': [1, 4001], 'm': [1, 4001], 'a': [1, 4001], 's': [1, 4001]
        }
        for name in self.workflows:
            rules = self.workflows[name][:-1]
            for rule in rules:
                _, axis, point, __ = rule
                if point not in self.points[axis]:
                    self.points[axis].append(point)

        for axis in self.points:
            self.points[axis] = sorted(self.points[axis])
        if self.verbose:
            for axis in self.points:
                print(axis + ':', self.points[axis])
        return self

    def calculate(self):
        xx = self.points['x']
        mm = self.points['m']
        aa = self.points['a']
        ss = self.points['s']
        total_iterations = (len(xx) - 1) * (len(mm) - 1) * (len(aa) - 1) * (len(ss) - 1)
        if self.verbose:
            print('total iterations', total_iterations)
        iteration = 0

        result = 0

        for ix in range(len(xx) - 1):
            for jm in range(len(mm) - 1):
                for ka in range(len(aa) - 1):
                    for ls in range(len(ss) - 1):
                        iteration += 1
                        x = xx[ix]
                        m = mm[jm]
                        a = aa[ka]
                        s = ss[ls]
                        is_valid = self.validate_part({'x': x, 'm': m, 'a': a, 's': s})
                        value = 0
                        if is_valid:
                            value = (xx[ix + 1] - x) * (mm[jm + 1] - m) * (aa[ka + 1] - a) * (ss[ls + 1] - s)
                            result += value
                        if self.verbose:
                            p = iteration * 100 / total_iterations
                            sp = '{:.3f}% {}/{}'.format(p, iteration, total_iterations)
                            print(sp, value)
        return result
