#!/Users/palutser/projects/aoc2023/venv/bin/python

from os import path

from days import SolveDay01x1, SolveDay01x2, SolveDay02x1, SolveDay02x2

DEFAULT_DAY = 2
variable = ''
solutions = {
    1: [SolveDay01x1, SolveDay01x2],
    2: [SolveDay02x1, SolveDay02x2]
}


def read_input(d: int) -> str:
    file_path = path.join('input', '{:02d}.txt'.format(d))
    with open(file_path) as f:
        return f.read()


if __name__ == '__main__':
    while True:
        print()
        print('Enter "q" to quit')
        user_input = input('Enter day (%d):' % DEFAULT_DAY)
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
            variant = 0
            for S in solutions[day]:
                variant += 1
                result = S().solve(read_input(day))
                print('Day %d Solution %d: %d' % (day, variant, result))

        except Exception as e:
            print(e)
            continue
