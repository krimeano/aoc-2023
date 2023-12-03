#!/Users/palutser/projects/aoc2023/venv/bin/python
from time import time
from os import path

from days.day01.solution import SolveDay01x1, SolveDay01x2
from days.day02.solution import SolveDay02x1, SolveDay02x2
from days.day03.solution import SolveDay03x1

DEFAULT_DAY = 3
variable = ''
solutions = {
    1: [SolveDay01x1, SolveDay01x2],
    2: [SolveDay02x1, SolveDay02x2],
    3: [SolveDay03x1],
}


def read_input(d: int) -> str:
    file_path = path.join('input', '{:02d}.txt'.format(d))
    with open(file_path) as f:
        return f.read()


if __name__ == '__main__':
    while True:
        print()
        print('Enter "q" to quit')
        user_input = input('Enter day (%d): ' % DEFAULT_DAY)
        day = 0
        user_input = user_input.strip()

        if user_input == 'q':
            exit(0)

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
                result = S().solve(read_input(day))
                print('Day %d Solution %d: %d' % (day, variant, result))

            elapsed_time = time() - started_at
            is_seconds = elapsed_time >= 10
            elapsed_time *= is_seconds and 1 or 1000
            suffix = is_seconds and '%ds' or '%dms'
            print('Execution time:', suffix % elapsed_time)

        except Exception as e:
            print(e)
            continue
