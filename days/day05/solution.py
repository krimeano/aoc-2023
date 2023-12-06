from days import SolveDay, sorted_to_tree

DIGITS = '1234567890'

MapItem = tuple[int, int, int]
Segment = tuple[int, int]
SegmentMap = dict[Segment: MapItem]


def find_stalk(leaf: int, tree: list[MapItem or None]) -> MapItem or None:
    ix = 0

    while ix < len(tree):
        stalk = tree[ix]

        if not stalk:
            return None

        if stalk[1] <= leaf < stalk[1] + stalk[2]:
            return stalk

        ix = 2 * ix + (leaf < stalk[1] and 1 or 2)

    return None


def map_to_segments(xxx: list[MapItem], ix: int) -> SegmentMap:
    return {(xx[ix], xx[ix] + xx[2]): xx for xx in xxx}


def split_segment(this: Segment, other_dots: list[int]) -> list[Segment]:
    (x0, x1) = this
    yy = [y for y in other_dots if x0 < y < x1]
    if not len(yy):
        return []
    y = yy.pop(0)
    return (split_segment((x0, y), yy) or [(x0, y)]) + (split_segment((y, x1), yy) or [(y, x1)])


def split_segments(this: SegmentMap, other: SegmentMap) -> SegmentMap:
    other_dots = sorted(set([yy[0] for yy in other] + [yy[1] for yy in other]))
    zzz: SegmentMap = {}
    for xx in this:
        item = this[xx]
        chunks = split_segment(xx, other_dots)
        if not chunks:
            zzz[xx] = item
        else:
            for zz in chunks:
                shift = zz[0] - xx[0]
                width = zz[1] - zz[0]
                zzz[zz] = (item[0] + shift, item[1] + shift, width)
    return zzz


def unify_maps(xxx: list[MapItem], yyy: list[MapItem]) -> list[MapItem]:
    if not xxx:
        return yyy

    images = map_to_segments(xxx, 0)
    reals = map_to_segments(yyy, 1)
    images = split_segments(images, reals)
    reals = split_segments(reals, images)

    zzz = []

    for xx in images:
        if xx in reals:
            zzz.append((reals[xx][0], images[xx][1], images[xx][2]))
        else:
            zzz.append(images[xx])

    for xx in reals:
        if xx not in images:
            zzz.append(reals[xx])
    return zzz


class SolveDay05x1(SolveDay):
    seeds: list[int] = []
    maps: list[list[MapItem]]
    unified_map: list[MapItem]
    trees: list[list[MapItem] or None]
    locations: list[int]

    def solve(self, text_input: str) -> int:
        if self.verbose:
            print()

        self.parse_data(self.get_lines(text_input))
        self.postprocess_maps()

        if self.verbose and False:
            print(self.seeds)
            for t in self.trees:
                print(t)

        self.find_locations()

        return min(self.locations)

    def parse_data(self, lines: list[str]):
        self.seeds = []
        self.maps = []
        current_map: list[MapItem] = []
        for line in lines:
            if line.startswith('seeds:'):
                self.seeds = [int(x) for x in line.split(': ').pop().split(' ') if x]
            elif line[0] in DIGITS:
                xx = [int(x) for x in line.split(' ') if x]
                current_map.append((xx[0], xx[1], xx[2]))
            else:
                if current_map:
                    self.maps.append(current_map)
                    current_map = []
        if current_map:
            self.maps.append(current_map)

    def postprocess_maps(self):
        self.trees = []
        self.unified_map = []
        for xx in self.maps:
            self.unified_map = unify_maps(self.unified_map, xx)
        self.trees.append(sorted_to_tree(sorted(self.unified_map, key=lambda x: x[1]), []))

    def find_locations(self):
        self.locations = [self.process_seed(seed) for seed in self.seeds]
        if self.verbose:
            print(self.locations)

    def process_seed(self, seed: int):
        leaf = seed
        trace: list[int] = [leaf]
        for tree in self.trees:
            stalk = find_stalk(leaf, tree)
            if stalk:
                leaf += stalk[0] - stalk[1]
            trace.append(leaf)
        if self.verbose:
            print('trace:', trace)
        return leaf


class SolveDay05x2(SolveDay05x1):
    def solve(self, text_input: str) -> int:
        return 0
