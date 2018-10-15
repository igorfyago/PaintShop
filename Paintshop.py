import sys

from src.Parser import Parser
from src.Solver import Solver


def paintshop_ide():
    import pathlib

    input_paths = [
        'input_0.txt',
        'input_1.txt',
        'input_2.txt',
        'input_3.txt',
        'input_messy_formatting.txt']

    for input_path in input_paths:
        path = pathlib.Path(pathlib.Path(__file__).parent / 'test' / input_path)
        solution = Solver(Parser(path)).solve()
        print(solution)
    # run: TestPaintshop.py for a pytest


def paintshop_console(args):
    for path in args:
        solution = Solver(Parser(path)).solve()
        print(solution)


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0:
        paintshop_ide()

    elif len(args) >= 1:
        paintshop_console(args)
