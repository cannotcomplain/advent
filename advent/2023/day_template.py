#!/usr/bin/env python3

from pathlib import Path
from typing import List, Union
import os


def create_line_generator(file_path, dtype=int):
    with open(file_path, 'r') as file:
        for line in file:
            try:
                yield [dtype(value) for value in line.strip().split()]
            except ValueError as e:
                print(f"Error converting line '{line.strip()}' to list of {dtype.__name__}: {e}")

class Advent:

    def __init__(self, input_file: str | os.PathLike ):
        """Initialize the file path and create a generator to read in the input file"""

        self.input_file = input_file
        self.input_generator = create_line_generator(input_file)

        # Run part 1
        self.sol1 = self.part1()
        # Run part 2
        self.sol2 = self.part2()

    def part1(self):
        """Part 1 solver."""

        return 'not done'


    def part2(self):
        """Part 2 solver."""

        return 'not done'


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("inputs") / (stem + ".txt")

    DaySolver = Advent(input_file)

    print(f"Part 1: {DaySolver.sol1}")
    print(f"Part 2: {DaySolver.sol2}")

