#!/Users/palutser/projects/aoc2023/venv/bin/python

import os

cwd = os.getcwd()
days_dir = 'days'
root = os.path.join(cwd, days_dir)

if not os.path.exists(root):
    raise 'No path "%s" in "%s"' % (days_dir, cwd)

os.chdir(root)

contents = [x for x in os.listdir('.') if x.startswith('day')]

last_day = max(int(x.startswith('day0') and x[4:] or x[3:]) for x in contents) or 0

if last_day >= 25:
    print('MERRY XMAS!')
    exit()

last_day_str = '{:02d}'.format(last_day)

new_day = last_day + 1
new_day_str = '{:02d}'.format(new_day)
new_folder = 'day{0}'.format(new_day_str)

print('creating day', new_day, 'in folder', new_folder)
os.mkdir(new_folder)
os.chdir(new_folder)

with open('__init__.py', 'w') as f:
    f.write('')

with open('solution.py', 'w') as f:
    f.writelines([
        'from days import SolveDay',
        '\n\n\nclass SolveDay{0}x1(SolveDay):'.format(new_day_str),
        '\n\n    def solve(self, text_input: str) -> int:',
        '\n        return 0',
        '\n\n\nclass SolveDay{0}x2(SolveDay{0}x1):'.format(new_day_str),
        '\n\n    def solve(self, text_input: str) -> int:',
        '\n        return 0',
    ])

with open('solution_test.py', 'w') as f:
    f.writelines([
        'from .solution import SolveDay{0}x1, SolveDay{0}x2'.format(new_day_str),
        '\ntext_input = """',
        '\n"""',
        '\n\n\ndef test_solution_1():',
        '\n    assert SolveDay{0}x1(True).solve(text_input) == 0'.format(new_day_str),
        '\n\n\ndef test_solution_2():',
        '\n    assert SolveDay{0}x2(True).solve(text_input) == 0'.format(new_day_str),
    ])
os.chdir(cwd)

main_content = []
with open('solve.py', 'r') as f:
    for x in f.readlines():
        if x.startswith('DEFAULT_DAY'):
            x = 'DEFAULT_DAY = {0}\n'.format(new_day)
        if x.startswith('from days.day{0}.solution import SolveDay{0}x1, SolveDay{0}x2\n'.format(last_day_str)):
            x += 'from days.day{0}.solution import SolveDay{0}x1, SolveDay{0}x2\n'.format(new_day_str)
        if x == '    {0}: [SolveDay{1}x1, SolveDay{1}x2],\n'.format(last_day, last_day_str):
            x += '    {0}: [SolveDay{1}x1, SolveDay{1}x2],\n'.format(new_day, new_day_str)
        main_content.append(x)

with open('solve.py', 'w') as f:
    f.writelines(main_content)
