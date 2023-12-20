def v_factor(a: int, b: tuple[int, int]) -> tuple[int, int]:
    return a * b[0], a * b[1]


def v_scalar(a: tuple[int, int], b: tuple[int, int]) -> int:
    return a[0] * b[0] + a[1] * b[1]


def v_add(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def v_len(a: tuple[int, int]) -> tuple[int, int]:
    return (a[0] ** 2 + a[1] ** 2) ** .5


MAX_LOSS = 999999
ORTS = ((-1, 0), (0, 1), (1, 0), (0, -1))
VECTORS = [xy for xy in ORTS] + [v_factor(2, xy) for xy in ORTS] + [v_factor(3, xy) for xy in ORTS]

CONSUME = {
    (-1, 0): (1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0),
    (0, 1): (0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0),
    (1, 0): (0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0),
    (0, -1): (0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1),
}

ONE_OF = (
    (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0),
    (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1),
    (1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
)

VEC_TO_STR = {
    (-1, 0): '^',
    (0, 1): '>',
    (1, 0): 'v',
    (0, -1): '<',
    (-2, 0): '^^',
    (0, 2): '>>',
    (2, 0): 'vv',
    (0, -2): '<<',
    (-3, 0): '^^^',
    (0, 3): '>>>',
    (3, 0): 'vvv',
    (0, -3): '<<<',
}


class Block:

    def __init__(self, iy: int, jx: int, heat_loss: int):
        self.iy = iy
        self.jx = jx
        self.heat_loss = heat_loss
        self.enters = {xy: MAX_LOSS for xy in VECTORS}
        self.exits = {xy: MAX_LOSS for xy in VECTORS}
        if not iy and not jx:
            for xy in ORTS:
                self.exits[xy] = 0

    def __str__(self):
        enters = ' '.join('{0}{1}'.format(VEC_TO_STR[xy], self.enters[xy]) for xy in self.enters)
        exits = ' '.join('{0}{1}'.format(VEC_TO_STR[xy], self.exits[xy]) for xy in self.exits)
        return '{0} - ({1},{2}):{3} - {4}'.format(enters, self.iy, self.jx, self.heat_loss, exits)

    def improve(self, other) -> bool:
        step = (self.iy - other.iy, self.jx - other.jx)
        should_review_exits = False
        for zk in range(len(CONSUME[step])):
            if not CONSUME[step][zk]:
                continue
            vec = VECTORS[zk]
            new_value = other.exits[vec] + self.heat_loss
            old_value = self.enters[vec]
            if new_value < old_value:
                self.enters[vec] = new_value
                should_review_exits = True

        if not should_review_exits:
            return False

        was_improved = False

        for zk in range(len(ONE_OF)):
            vec = VECTORS[zk]
            old_value = self.exits[vec]
            new_value = min([self.enters[VECTORS[al]] for al in range(len(ONE_OF[zk])) if ONE_OF[zk][al]])
            if new_value < old_value:
                self.exits[vec] = new_value
                was_improved = True

        return was_improved
