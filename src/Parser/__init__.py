from collections import namedtuple

trim = lambda line: line.rstrip('\n').replace(' ', '').replace('\t', '').strip()
combine_every_n = lambda line, n: (line[i:i + n] for i in range(0, len(line), n))
preferences = lambda line: dict((int(string[0]), str(string[1])) for string in combine_every_n(line, 2))


class Parser:

    def __init__(self, path):
        self.path = str(path)

        self.input_lines = [trim(line) for line in open(self.path, 'r').read().splitlines() if len(trim(line)) > 0]

        self.styles_solution = {k: 'G' for k, v in ((color_i + 1, 'G') for color_i in range(int(self.input_lines[0])))}

        self.Customers = namedtuple('Customers', ['id', 'preferences', 'preferences_count'])

        self.customers = sorted(
            [self.Customers(id=row, preferences=preferences(line), preferences_count=len(preferences(line))) for row, line in enumerate(self.input_lines[1:])]
            , key=lambda customer: customer.preferences_count)
