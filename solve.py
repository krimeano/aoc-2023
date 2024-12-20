#!/Users/palutser/projects/aoc2023/venv/bin/python
from os import path
from time import time

from days.day01.solution import SolveDay01x1, SolveDay01x2
from days.day02.solution import SolveDay02x1, SolveDay02x2
from days.day03.solution import SolveDay03x1, SolveDay03x2
from days.day04.solution import SolveDay04x1, SolveDay04x2
from days.day05.solution import SolveDay05x1, SolveDay05x2
from days.day07.solution import SolveDay07x1, SolveDay07x2
from days.day08.solution import SolveDay08x1, SolveDay08x2
from days.day09.solution import SolveDay09x1, SolveDay09x2
from days.day10.solution import SolveDay10x1, SolveDay10x2
from days.day11.solution import SolveDay11x1, SolveDay11x2
from days.day12.solution import SolveDay12x1, SolveDay12x2
from days.day13.solution import SolveDay13x1, SolveDay13x2
from days.day14.solution import SolveDay14x1, SolveDay14x2
from days.day15.solution import SolveDay15x1, SolveDay15x2
from days.day16.solution import SolveDay16x1, SolveDay16x2
from days.day17.solution import SolveDay17x1, SolveDay17x2
from days.day18.solution import SolveDay18x1, SolveDay18x2
from days.day19.solution import SolveDay19x1, SolveDay19x2
from days.day20.solution import SolveDay20x1, SolveDay20x2
from days.day21.solution import SolveDay21x1, SolveDay21x2
from days.day22.solution import SolveDay22x1, SolveDay22x2
from days.day23.solution import SolveDay23x1, SolveDay23x2
from days.day24.solution import SolveDay24x1, SolveDay24x2

DEFAULT_DAY = 24
variable = ''
solutions = {
    1: [SolveDay01x1, SolveDay01x2],
    2: [SolveDay02x1, SolveDay02x2],
    3: [SolveDay03x1, SolveDay03x2],
    4: [SolveDay04x1, SolveDay04x2],
    5: [SolveDay05x1, SolveDay05x2],
    7: [SolveDay07x1, SolveDay07x2],
    8: [SolveDay08x1, SolveDay08x2],
    9: [SolveDay09x1, SolveDay09x2],
    10: [SolveDay10x1, SolveDay10x2],
    11: [SolveDay11x1, SolveDay11x2],
    12: [SolveDay12x1, SolveDay12x2],
    13: [SolveDay13x1, SolveDay13x2],
    14: [SolveDay14x1, SolveDay14x2],
    15: [SolveDay15x1, SolveDay15x2],
    16: [SolveDay16x1, SolveDay16x2],
    17: [SolveDay17x1, SolveDay17x2],
    18: [SolveDay18x1, SolveDay18x2],
    19: [SolveDay19x1, SolveDay19x2],
    20: [SolveDay20x1, SolveDay20x2],
    21: [SolveDay21x1, SolveDay21x2],
    22: [SolveDay22x1, SolveDay22x2],
    23: [SolveDay23x1, SolveDay23x2],
    24: [SolveDay24x1, SolveDay24x2],
}


def read_input(d: int) -> str:
    file_path = path.join('input', '{:02d}.txt'.format(d))
    with open(file_path) as f:
        return f.read()


if __name__ == '__main__':
    verbose = False
    first_cycle = True
    while True:
        print()
        print('Enter "q" to quit')
        user_input = input('Enter day (%d): ' % DEFAULT_DAY)
        day = 0
        user_input = user_input.strip()

        if user_input == 'q':
            exit(0)

        if user_input == 'v':
            verbose = not verbose
            print('toggle verbose -> ', verbose)
            continue

        try:
            day = user_input and int(user_input) or DEFAULT_DAY
        except:
            print('"%s" is not a number' % user_input)
            continue

        if day not in solutions:
            print('day %d is not solved yet' % day)

        try:
            started_at = time()
            variant = 0
            for S in solutions[day]:
                variant += 1
                result = S(verbose).solve(read_input(day))
                print('Day %d Solution %d: %d' % (day, variant, result))

            elapsed_time = time() - started_at
            is_seconds = elapsed_time >= 10
            elapsed_time *= is_seconds and 1 or 1000
            suffix = is_seconds and '%ds' or '%dms'
            print('Execution time:', suffix % elapsed_time)

        except Exception as e:
            print(e)
            continue
