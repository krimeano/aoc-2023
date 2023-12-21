from days import SolveDay

Trench = tuple[tuple[int, int], tuple[int, int]]


class SolveDay18x1(SolveDay):

    def solve(self, text_input: str) -> int:
        min_x = x = max_x = min_y = y = max_y = 0
        trenches: list[Trench] = []

        for line in self.get_lines(text_input):
            x0, y0 = x, y
            parts = line.split(' ')
            direction = parts[0]
            length = int(parts[1])
            if direction == 'L':
                x -= length
                min_x = min([min_x, x])
            if direction == 'R':
                x += length
                max_x = max([max_x, x])
            if direction == 'U':
                y -= length
                min_y = min([min_y, y])
            if direction == 'D':
                y += length
                max_y = max([max_y, y])
            trenches.append(((min([x0, x]), min([y0, y])), (max([x, x0]), max([y, y0]))))
            print(direction, length, '->', x, y)
        print(len(trenches))
        print(min_x, max_x, min_y, max_y)
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        landscape = [['.'] * width for _ in range(height)]
        for trench in trenches:
            (x0, y0), (x1, y1) = trench
            for iy in range(y0 - min_y, y1 - min_y + 1):
                for jx in range(x0 - min_x, x1 - min_x + 1):
                    landscape[iy][jx] = '#'

        filling = {(1 - min_x, 1 - min_y)}
        landscape[1 - min_y][1 - min_x] = '#'
        while len(filling):
            (x0, y0) = filling.pop()
            for (x, y) in ((x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1)):
                if 0 <= x < width and 0 <= y < height and landscape[y][x] == '.':
                    landscape[y][x] = '#'
                    filling.add((x, y))
        for row in landscape:
            print(''.join(row))
        return sum(sum(cell == '#' and 1 or 0 for cell in row) for row in landscape)


class SolveDay18x2(SolveDay18x1):

    def solve(self, text_input: str) -> int:
        return 0
