from days import SolveDay

ORTS = {
    (-1, 0): '^',
    (0, 1): '>',
    (1, 0): 'v',
    (0, -1): '<'
}


def get_neighbours(xy: tuple[int, int]) -> list[tuple[int, int]]:
    return [(xy[0] + d[0], xy[1] + d[1]) for d in ORTS]


class SolveDay23x1(SolveDay):
    lines: list[str]
    size: int
    nodes: list[tuple[int, int]]

    def solve(self, text_input: str) -> int:
        self.parse_input(text_input)
        return 0

    def parse_input(self, text_input: str):
        self.lines = self.get_lines(text_input)
        self.size = len(self.lines)
        self.nodes = [(0, 1), (self.size, self.size - 1)]
        considered = {(0, 1)}
        from_node = (0, 1)


class SolveDay23x2(SolveDay23x1):

    def solve(self, text_input: str) -> int:
        return 0
