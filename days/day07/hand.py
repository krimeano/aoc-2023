LABELS = '23456789TJQKA'
VALUES = 'bcdefghijklmn'


class Hand:
    values = {LABELS[ix]: VALUES[ix] for ix in range(len(LABELS))}

    def __init__(self, cards: str, bid: str):
        self.cards = cards
        self.bid = int(bid)
        self.sorting = self.get_combination() + self.get_str_value()

    def __str__(self):
        return self.cards

    def get_combination(self) -> str:
        matches = self.get_matches()
        return ''.join(str(x) for x in sorted([matches[x] for x in matches], reverse=True))

    def get_matches(self) -> dict[str: int]:
        matches: dict[str: int] = {}
        for x in self.cards:
            if x not in matches:
                matches[x] = 0
            matches[x] += 1
        return matches

    def get_str_value(self) -> str:
        return ''.join(self.values[x] for x in self.cards)
