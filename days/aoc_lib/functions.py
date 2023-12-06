from typing import TypeVar

T = TypeVar('T')


def sorted_to_tree(ss: list[T], tree: list[T or None], ix=0) -> list[T or None]:
    if not ss:
        return tree
    out = [stalk for stalk in tree]
    if len(tree) <= ix:
        out += [None] * (ix + 1 - len(tree))
    middle_ix = len(ss) // 2
    out[ix] = ss[middle_ix]
    out = sorted_to_tree(ss[:middle_ix], out, 2 * ix + 1)
    out = sorted_to_tree(ss[middle_ix + 1:], out, 2 * ix + 2)
    return out
