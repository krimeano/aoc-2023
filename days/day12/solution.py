from days import SolveDay


class SolveDay12x1(SolveDay):
    repetitions = 1

    def solve(self, text_input: str) -> int:
        total = 0
        for line in self.get_lines(text_input):
            [profile, str_items] = line.split(' ')
            total += ways_to_fit('?'.join([profile] * self.repetitions), [int(x) for x in str_items.split(',')] * self.repetitions)
        if self.verbose:
            for x in sorted(cached_fit):
                print('can_fit', x, cached_fit[x])
        return total


class SolveDay12x2(SolveDay12x1):
    repetitions = 5


cached_ways: dict[tuple[str, str]: int] = {}


def ways_to_fit(profile: str, items: list[int]) -> int:
    key = (profile, ','.join([str(x) for x in items]))
    if key not in cached_ways:
        cached_ways[key] = calculate_ways_to_fit(profile, items)
    # print('ways_to_fit', key, cached_ways[key])
    return cached_ways[key]


def calculate_ways_to_fit(profile: str, items: list[int]) -> int:
    if not items:
        return '#' not in profile and 1 or 0

    if not profile:
        return 0

    min_width = sum(items) + len(items) - 1

    if min_width > len(profile):
        return 0

    total = 0

    for ix in range(0, len(profile) - min_width + 1):
        width = items[0]
        prefix_width = ix + width + 1

        if can_fit(profile[:prefix_width], width, ix):
            total += ways_to_fit(profile[prefix_width:], items[1:])

    return total


cached_fit: dict[tuple[str, int, int]: bool] = {}


def can_fit(profile: str, width: int, pos: 0) -> bool:
    key = (profile, width, pos)
    if key not in cached_fit:
        cached_fit[key] = calculate_can_fit(profile, width, pos)
        # print('can_fit', key, cached_fit[key])
    return cached_fit[key]


def calculate_can_fit(profile: str, width: int, pos: 0) -> bool:
    if width + pos > len(profile):
        return False

    if pos and '#' in profile[:pos]:
        return False

    if pos + width < len(profile) and profile[width + pos] == '#':
        return False

    for ix in range(pos, pos + width):
        if profile[ix] == '.':
            return False

    return True
