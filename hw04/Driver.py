"""The driver program.

    This program implements the functionality of Converter.py
    according to the specifications of comp398 hw04 assignment
    as outlined in the commented code.
"""

import Converter


def main():
    """Demonstrates the functionality of Converter.py
    """

    print Converter.Converter("test.md")
    print "\n\n\n\n\n"
    print Converter.Converter("readme.md")


if __name__ == "__main__":
    main()
