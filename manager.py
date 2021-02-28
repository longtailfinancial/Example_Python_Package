"""
manager offers a simple command line interface into common tasks
that are often needed when developing a package.
"""

import argparse
import subprocess as sp
import sys


def run_tests(cmd: str = "pytest") -> None:
    """
    run different types of tests
    :param: cmd defualts to pytest, which just runs all tests
    """
    try:
        sp.run(cmd, shell=True, check=True)
    except sp.CalledProcessError as error:
        sys.stderr.write(f"{error}\n")


def preprocess() -> None:
    """
    preprocess performs a series of checks to make sure
    the manager can actually be used
    """


def main(arg):
    """
    main routine
    """
    if arg.runtests:
        run_tests()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("runtests", help="run all tests", type=str)
    args = parser.parse_args()

    main(args)
