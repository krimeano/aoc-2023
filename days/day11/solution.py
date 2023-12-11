from days import SolveDay


class SolveDay11x1(SolveDay):
    age = 1
    galaxies: list[tuple[int, int]]
    empty_spaces_y: set[int]
    empty_spaces_x: set[int]

    def solve(self, text_input: str) -> int:
        self.find_galaxies(self.get_lines(text_input))
        self.expand_galaxies()

        return self.calculate_distances()

    def find_galaxies(self, lines: list[str]):
        if self.verbose:
            for line in lines:
                print(line)
        width = len(lines[0])
        height = len(lines)

        self.galaxies = []
        settled_xx = set()
        settled_yy = set()

        for iy in range(width):
            for jx in range(height):
                if lines[iy][jx] == '#':
                    self.galaxies.append((iy, jx))
                    settled_xx.add(jx)
                    settled_yy.add(iy)

        self.empty_spaces_x = set(x for x in range(width) if x not in settled_xx)
        self.empty_spaces_y = set(y for y in range(height) if y not in settled_yy)

        if self.verbose:
            print(self.galaxies)
            print(self.empty_spaces_y)
            print(self.empty_spaces_x)

    def expand_galaxies(self):
        for ix in range(len(self.galaxies)):
            y, x = self.galaxies[ix]
            y += len([z for z in self.empty_spaces_y if z < y]) * self.age
            x += len([z for z in self.empty_spaces_x if z < x]) * self.age
            self.galaxies[ix] = (y, x)
        if self.verbose:
            print(self.galaxies)

    def calculate_distances(self) -> int:
        total = 0
        size = len(self.galaxies)
        for ix in range(size - 1):
            y0, x0 = self.galaxies[ix]
            for jy in range(ix + 1, size):
                y1, x1 = self.galaxies[jy]
                total += abs(y1 - y0) + abs(x1 - x0)
        return total


class SolveDay11x2(SolveDay11x1):
    age = 999999
