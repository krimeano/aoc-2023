from days import SolveDay

# is_high, src, dest
Signal = tuple[bool, str, str]
Bus = list[Signal]


class Module:
    type = ''

    def __init__(self, name: str, destinations: list[str]):
        self.name = name
        self.destinations = destinations
        self.inputs: dict[str, bool] = {}

    def add_input(self, name: str):
        self.inputs[name] = False

    def receive(self, signal: Signal) -> list[Signal]:
        if self.should_ignore(*signal):
            return []

        self.handle(*signal)

        value = self.is_high_output()

        return [(value, self.name, x) for x in self.destinations]

    def should_ignore(self, *signal: Signal) -> bool:
        return False

    def handle(self, *signal: Signal) -> None:
        return

    def is_high_output(self) -> bool:
        return False

    def __str__(self):
        return self.type + self.name + '(' + ','.join(self.inputs) + ')' + ' -> ' + ','.join(self.destinations)


class FlipFlop(Module):
    type = '%'
    is_on = False

    def should_ignore(self, is_high: bool, *args) -> bool:
        return is_high

    def handle(self, is_high: bool, *args):
        self.is_on = not self.is_on

    def is_high_output(self) -> bool:
        return self.is_on


class Conjunction(Module):
    type = '&'

    def handle(self, is_high: bool, name: str, *args):
        self.inputs[name] = is_high

    def is_high_output(self) -> bool:
        for ix in self.inputs:
            if not self.inputs[ix]:
                return True
        return False


def module_factory(full_name: str, destinations: list[str]) -> Module:
    if full_name == 'button' or full_name == 'broadcaster' or full_name == 'output':
        return Module(full_name, destinations)

    module_type = full_name[0]
    name = ''.join(full_name[1:])

    if module_type == '%':
        return FlipFlop(name, destinations)

    if module_type == '&':
        return Conjunction(name, destinations)

    raise 'Unknown module type "{}"'.format(full_name)


class SolveDay20x1(SolveDay):
    count_high: int
    count_low: int
    bus: Bus
    modules: dict[str, Module]

    def solve(self, text_input: str) -> int:
        self.reset()
        self.parse_input(text_input)

        for _ in range(1000):
            self.push_button()
        return self.count_high * self.count_low

    def reset(self):
        self.count_high = 0
        self.count_low = 0
        self.bus = []
        self.modules = {
            'button': module_factory('button', ['broadcaster'])
        }

    def parse_input(self, text_input: str):
        for line in self.get_lines(text_input):
            src, dest = line.split(' -> ')
            dd = dest.split(', ')
            module = module_factory(src, dd)
            self.modules[module.name] = module

        self.update_conjunctions()

        if self.verbose:
            for name in self.modules:
                print(self.modules[name])

    def update_conjunctions(self):
        for src in self.modules:
            module = self.modules[src]
            for dst in module.destinations:
                if dst in self.modules:
                    self.modules[dst].add_input(src)

    def push_button(self):
        self.send((False, 'button', 'broadcaster'))
        while len(self.bus):
            x = self.bus.pop(0)
            name = x[-1]
            if name in self.modules:
                for y in self.modules[name].receive(x):
                    self.send(y)

    def send(self, signal: Signal):
        if self.verbose:
            print('SEND', signal)
        if signal[0]:
            self.count_high += 1
        else:
            self.count_low += 1
        self.bus.append(signal)


class SolveDay20x2(SolveDay20x1):
    machine_started = False

    def solve(self, text_input: str) -> int:
        self.machine_started = False
        count_pushes = 0
        self.reset()
        self.parse_input(text_input)

        while not self.machine_started:
            count_pushes += 1
            if not count_pushes % 10 ** 6:
                print('push number', count_pushes)
            self.push_button()
        return count_pushes

    def send(self, signal: Signal):
        if self.verbose:
            print('SEND', signal)

        if signal[-1] == 'rx' and not signal[0]:
            self.machine_started = True

        self.bus.append(signal)
