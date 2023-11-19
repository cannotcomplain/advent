#!/usr/bin/env python3

import os
import heapq
from pathlib import Path
from typing import List, Union
from ipdb import set_trace as db


class Advent:

    def __init__(self, input_file: str | os.PathLike ):
        """Initialize the file path and create a generator to read in the input file"""

        self.input_file = input_file

        # Run part 1
        self.sol1 = self.part1()
        # Run part 2
        self.sol2 = self.part2()

    def part1(self):
        """Find the elf with the most calories. Each elves pack is separated by a blank line"""

        highest_calorie_pack = 0
        current_pack = 0

        line_generator = self.create_line_generator(self.input_file)
        for line in line_generator:
            if line == '' or line.isspace():
                if current_pack > highest_calorie_pack:
                    highest_calorie_pack = current_pack
                current_pack = 0
            else:
                try:
                    current_pack += int(line)
                except ValueError as e:
                    print(f"Could not convert line {line} to int")

        # make sure to check last row, if it isn't a blank space
        if current_pack != 0:
            if current_pack > highest_calorie_pack:
                highest_calorie_pack = current_pack

        return highest_calorie_pack


    def part2(self):
        """
        Find the three elves with the most calories. Each elves pack is separated by a blank line.
        How many calories to all three of those elves have combined?
        """
        highest_calorie_packs = [0, 0, 0] # three packs in increasing calorie order
        current_pack = 0

        line_generator = self.create_line_generator(self.input_file)
        for line in line_generator:
            if line == '' or line.isspace():
                test_packs = highest_calorie_packs + [current_pack]
                highest_calorie_packs = heapq.nlargest(3, test_packs)
                current_pack = 0
            else:
                try:
                    current_pack += int(line)
                except ValueError as e:
                    print(f"Could not convert line {line} to int")

        # make sure to check last row, if it isn't a blank space
        if current_pack != 0:
            test_packs = highest_calorie_packs + [current_pack]
            highest_calorie_packs = heapq.nlargest(3, test_packs)

        total_calories = sum(highest_calorie_packs)
        return total_calories


    @staticmethod
    def create_line_generator(file_path):
        with open(file_path, 'r') as file:
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

