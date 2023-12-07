LABELS = '23456789TJQKA'
VALUES = 'bcdefghijklmn'
MAP = {LABELS[ix]: VALUES[ix] for ix in range(len(LABELS))}

JOKER_LABELS = 'J23456789TQKA'
JOKER_VALUES = 'abcdefghijlmn'
JOKER_MAP = {JOKER_LABELS[ix]: JOKER_VALUES[ix] for ix in range(len(JOKER_LABELS))}


class Hand:
    def __init__(self, with_jokers: bool, cards: str, bid: str):
        self.with_jokers = with_jokers
        self.cards = cards
        self.bid = int(bid)
        self.sorting = self.get_combination() + self.get_str_value()

    def __str__(self):
        return self.cards

    def get_combination(self) -> str:
        matches: dict[str: int] = {}
        jokers = 0

        for x in self.cards:

            if x == 'J' and self.with_jokers:
                jokers += 1
                continue

            if x not in matches:
                matches[x] = 0

            matches[x] += 1

        if jokers == 5:
            return '5'

        xx = sorted([matches[x] for x in matches], reverse=True)
        xx[0] += jokers

        return ''.join(str(x) for x in xx)

    def get_str_value(self) -> str:
        ss = self.with_jokers and JOKER_MAP or MAP
        return ''.join(ss[x] for x in self.cards)
