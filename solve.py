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

DEFAULT_DAY = 12
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
