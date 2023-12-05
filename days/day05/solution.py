from days import SolveDay

DIGITS = '1234567890'


def sorted_to_tree(ss: list[tuple[int, int, int]], tree: list[tuple[int, int, int] or None], ix=0) -> list[tuple[int, int, int] or None]:
    if not ss:
        return tree
    out = [stalk for stalk in tree]
    if len(tree) <= ix:
        out += [None] * (ix + 1 - len(tree))
    middle_ix = len(ss) // 2
    out[ix] = ss[middle_ix]
    out = sorted_to_tree(ss[:middle_ix], out, 2 * ix + 1)
    out = sorted_to_tree(ss[middle_ix + 1:], out, 2 * ix + 2)
    return out


def find_stalk(leaf: int, tree: list[tuple[int, int, int] or None]) -> tuple[int, int, int] or None:
    ix = 0

    while ix < len(tree):
        stalk = tree[ix]

        if not stalk:
            return None

        if stalk[0] <= leaf < stalk[1]:
            return stalk

        ix = 2 * ix + (leaf < stalk[0] and 1 or 2)

    return None


class SolveDay05x1(SolveDay):
    seeds: list[int] = []
    trees: list[list[tuple[int, int, int]] or None]
    locations: list[int]

    def solve(self, text_input: str) -> int:
        if self.verbose:
            print()

        self.parse_data(self.get_lines(text_input))

        if self.verbose:
            print(self.seeds)
            for t in self.trees:
                print(t)

        self.locations = [self.process_seed(seed) for seed in self.seeds]

        if self.verbose:
            print(self.locations)

        return min(self.locations)

    def parse_data(self, lines: list[str]):
        self.seeds = []
        self.trees = []
        current_map: list[tuple[int, int, int]] = []
        for line in lines:
            if line.startswith('seeds:'):
                self.seeds = [int(x) for x in line.split(': ').pop().split(' ') if x]
            elif line[0] in DIGITS:
                xx = [int(x) for x in line.split(' ') if x]
                current_map.append((xx[1], xx[1] + xx[2], xx[0]))
            else:
                if current_map:
                    self.trees.append(sorted_to_tree(sorted(current_map), []))
                    current_map = []
        if current_map:
            self.trees.append(sorted_to_tree(sorted(current_map), []))

    def process_seed(self, seed: int):
        leaf = seed
        trace: list[int] = [leaf]
        for tree in self.trees:
            stalk = find_stalk(leaf, tree)
            if stalk:
                leaf += stalk[2] - stalk[0]
            trace.append(leaf)
        if self.verbose:
            print('trace:', trace)
        return leaf


class SolveDay05x2(SolveDay05x1):
    def solve(self, text_input: str) -> int:
        return 0
