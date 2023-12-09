class Progression:
    def __init__(self, sequence: list[int]):
        self.sequence = sequence
        xxx: list[list[int]] = []
        xx = sequence
        while [x for x in xx if x] and len(xx) > 1:
            xxx.append(xx)
            xx = [xx[ix] - xx[ix - 1] for ix in range(1, len(xx))]
        self.hypersequence = xxx[::-1]
        self.cds: list[int] = [xx[0] for xx in xxx]

    def next(self) -> int:
        d = 0
        for xx in self.hypersequence:
            xx.append(xx[-1] + d)
            d = xx[-1]
        return d

    def prev(self) -> int:
        d = 0
        for xx in self.hypersequence:
            xx.insert(0, xx[0] - d)
            d = xx[0]
        return d
