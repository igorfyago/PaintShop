from collections import namedtuple

trim = lambda line: (line.rstrip('\n').replace(' ', '').replace('\t', '').strip())
split_preferences = lambda line: line.replace('G', 'G ').replace('M', 'M ').rstrip(' ').split(' ')
preferences = lambda line: dict((int(string[:-1]), str(string[-1])) for string in split_preferences(line))


class Parser:

    def __init__(self, path):

        self.path = str(path)

        self.input_lines = [trim(line) for line in open(self.path, 'r').read().splitlines() if len(trim(line)) > 0]

        self.styles_solution = {k: 'G' for k, v in ((color_i + 1, 'G') for color_i in range(int(self.input_lines[0])))}

        self.Customers = namedtuple('Customers', ['preferences', 'preferences_count'])

        self.customers = sorted(
            tuple(self.Customers(preferences=preferences(line), preferences_count=len(preferences(line))) for line in self.input_lines[1:])
            , key=lambda customer: customer.preferences_count)
