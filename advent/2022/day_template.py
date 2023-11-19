#!/usr/bin/env python3

import os
import ipdb
from pathlib import Path
from typing import List, Union


class Advent:
    def __init__(self, input_file: str | os.PathLike ):
        """Initialize the file path and create a generator to read in the input file"""

        self.input_file = input_file

        # Run part 1
        self.sol1 = self.part1()
        # Run part 2
        self.sol2 = self.part2()

    def part1(self):
        """Part 1 solver."""

#        line_generator = self.create_line_generator()
#        for line in line_generator:
#             pass

        return 'not done'


    def part2(self):
        """Part 2 solver."""

#        line_generator = self.create_line_generator()
#        for line in line_generator:
#             pass

        return 'not done'

    def create_line_generator(self):
            with open(self.input_file, 'r') as file:
                for line in file:
                    try:
                        yield line.strip()
                    except ValueError as e:
                        print(f"Error returning line '{line.strip()}'")


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("inputs") / (stem + ".txt")

    DaySolver = Advent(input_file)

    print(f"Part 1: {DaySolver.sol1}")
    print(f"Part 2: {DaySolver.sol2}")

