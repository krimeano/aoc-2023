MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


class Game:
    def __init__(self, line: str):
        [name, xxxx] = line.split(': ')
        self.id = int(name.split(' ')[-1])
        self.is_possible = True

        fewest = {
            'red': 1,
            'green': 1,
            'blue': 1
        }

        for xxx in xxxx.split('; '):
            for xx in xxx.split(', '):
                [x, color] = xx.split(' ')
                n = int(x)

                if color not in MAX_CUBES or int(n) > MAX_CUBES[color]:
                    self.is_possible = False

                if color not in fewest:
                    fewest[color] = 0

                if n > fewest[color]:
                    fewest[color] = n

        self.power = fewest['red'] * fewest['green'] * fewest['blue']
