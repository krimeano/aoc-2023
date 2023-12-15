from functools import reduce

from days import SolveDay


def get_hash(cc: str):
    return reduce(lambda h, x: ((h + x) * 17) % 256, [0] + [ord(c) for c in cc])


class SolveDay15x1(SolveDay):

    def solve(self, text_input: str) -> int:
        return sum(get_hash(cc) for cc in self.get_lines(text_input).pop().split(','))


class SolveDay15x2(SolveDay15x1):

    def solve(self, text_input: str) -> int:
        boxes: dict[int: list[str]] = {}
        forces: dict[str: int] = {}

        for lens in self.get_lines(text_input).pop().split(','):
            [label, force] = lens.endswith('-') and [lens[:-1], '0'] or lens.split('=')
            force = int(force)
            forces[label] = force
            ix = get_hash(label)

            if ix not in boxes:
                boxes[ix] = []

            if label in boxes[ix]:
                if not force:
                    boxes[ix].remove(label)
            else:
                if force:
                    boxes[ix].append(label)

        return sum(sum((ix + 1) * (jy + 1) * forces[boxes[ix][jy]] for jy in range(len(boxes[ix]))) for ix in boxes if boxes[ix])
