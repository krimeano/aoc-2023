from .hand import Hand, LABELS, VALUES

JOKER = 'J'
JOKER_MAP = {LABELS[ix]: VALUES[ix] for ix in range(len(LABELS))}
JOKER_MAP[JOKER] = 'a'


class HandJoker(Hand):
    values = JOKER_MAP

    def __str__(self):
        return '*'.join(self.cards.split(JOKER))

    def get_combination(self) -> str:
        matches: dict[str: int] = self.get_matches()
        jokers = 0
        if JOKER in matches:
            jokers = matches[JOKER]
            matches[JOKER] = 0
        xx = sorted([matches[x] for x in matches], reverse=True)
        xx[0] += jokers
        return '{0:0<5}'.format(''.join(str(x) for x in xx))
