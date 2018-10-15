NO_SOLUTION = 'No solution exists'


class Solver:

    @staticmethod
    def to_string(arg):
        if type(arg) is dict:
            arg = ' '.join(list(arg.values()))
        elif type(arg) is list:
            arg = ' '.join(arg)
        return arg

    def __init__(self, parser):

        self.parser = parser

        self.customers = self.parser.customers

    def solve(self):

        def satisfied_check(customer):
            for color, pref_style in customer.preferences.items():
                if self.parser.styles_solution[color] == pref_style:
                    return True, None, None
            return False, color, pref_style

        def run():
            for stage in iter(['solve', 'validate']):
                for customer in self.customers:
                    satisfied, update_color, update_style = satisfied_check(customer)
                    if not satisfied:
                        if stage == 'solve' and update_style == 'M':
                            self.parser.styles_solution[update_color] = 'M'
                        else:
                            return NO_SOLUTION
            return self.to_string(self.parser.styles_solution)

        return run()
