"""
# Run all tests (--test)
python manager.py -t all

# Run smoke tests (--test)
python manager.py -t smoke

# Run pytest on specific module or function by specifying it by name
python manager.py -t test_some_function_name

# Show all environment variables (debug)
python manager.py -d
"""

import argparse
import os
import subprocess as sp
import sys


def debug_print() -> None:
    """
    print out env variables
    """
    sp.run('which python', shell=True, check=True)
    sp.run('which pytest', shell=True, check=True)
    sp.run('which mypy', shell=True, check=True)
    sp.run('which stubgen', shell=True, check=True)


def run_tests(cmd: str = "pytest") -> None:
    """
    run different types of tests
    :param: cmd defualts to pytest, which just runs all tests
    """
    try:
        sp.run(cmd, shell=True, check=True)
    except sp.CalledProcessError as error:
        sys.stderr.write(f"{error}\n")


def static_analyzer() -> None:
    """
    Run the mypy static anaylzer on entire project
    """
    ...


def generate_stubs() -> None:
    """
    Generate file stubs for all modules
    and sub-packages
    """
    ...


def main(arg):
    """
    main routine
    """
    if not os.getenv('VIRTUAL_ENV'):
        sys.stderr.write('❌ Virtual environment not activated\n')
        sys.exit(1)

    if arg.debug:
        debug_print()

    if arg.test:
        if arg.test in "all":
            run_tests()
        elif arg.test in "smoke":
            print("Running smoke tests")
        else:
            print(f"Running tests for: {arg.test}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d",
                        "--debug",
                        help="print out all environment variables",
                        action="store_true")

    parser.add_argument("-t",
                        "--test",
                        help="all, smoke, module/function/ name",
                        type=str)
    args = parser.parse_args()

    main(args)
