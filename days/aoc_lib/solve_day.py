class SolveDay:
    ignore_empty_lines = True

    def __init__(self, verbose=False):
        self.verbose = verbose

    def solve(self, text_input: str) -> int:
        raise 'not implemented'

    def get_lines(self, text_input):
        return [y for y in [x.strip() for x in text_input.split('\n')] if len(y) > 0 or not self.ignore_empty_lines]
