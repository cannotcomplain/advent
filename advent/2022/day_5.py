#!/usr/bin/env python3

import os
import ipdb
import re
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

        stacks = {}
        line_generator = self.create_line_generator()
        for idx, line in enumerate(line_generator):
            pattern = r"\[[A-Za-z]\]"  # This pattern matches [X], where X can be any letter (upper or lower case)
            matches = re.findall(pattern, line)

            if matches:
                # split the row into crates
                layer = [line[i:i+4] for i in range(0, len(line), 4)]
                N_stacks = len(layer)
                if N_stacks > len(stacks):
                    for n in range(len(stacks), N_stacks):
                        stacks[n+1] = []
                for idx, col in enumerate(layer):
                    # get the letter of the crate
                    l = re.findall(r"(?i)[A-Z]+", col)
                    if len(l) > 0:
                        stacks[idx+1].append(l[0])

            else:
                break
#        print(f"Length stacks: {len(stacks)}")
#        print(f"Size of each stack:")
#        for ii in range(len(stacks)):
#            print(f"{ii+1}: {len(stacks[ii])}")
        for idy, line in enumerate(line_generator):
            pattern = r"[0-9]+"
            matches = re.findall(pattern, line)
            if matches:
                N_crates, from_bin, to_bin = map(lambda x: int(x), matches)
                for ii in range(N_crates):
                    stacks[to_bin].insert(0, stacks[from_bin].pop(0))

        tops = [stacks[key][0] for key in sorted(stacks.keys())]
        return "".join(tops)


    def part2(self):
        """Part 2 solver."""
        stacks = {}
        line_generator = self.create_line_generator()
        for idx, line in enumerate(line_generator):
            pattern = r"\[[A-Za-z]\]"  # This pattern matches [X], where X can be any letter (upper or lower case)
            matches = re.findall(pattern, line)

            if matches:
                # split the row into crates
                layer = [line[i:i+4] for i in range(0, len(line), 4)]
                N_stacks = len(layer)
                if N_stacks > len(stacks):
                    for n in range(len(stacks), N_stacks):
                        stacks[n+1] = []
                for idx, col in enumerate(layer):
                    # get the letter of the crate
                    l = re.findall(r"(?i)[A-Z]+", col)
                    if len(l) > 0:
                        stacks[idx+1].append(l[0])

            else:
                break
#        print(f"Length stacks: {len(stacks)}")
#        print(f"Size of each stack:")
#        for ii in range(len(stacks)):
#            print(f"{ii+1}: {len(stacks[ii])}")
        for idy, line in enumerate(line_generator):
            pattern = r"[0-9]+"
            matches = re.findall(pattern, line)
            if matches:
                N_crates, from_bin, to_bin = map(lambda x: int(x), matches)
                insert_list = []
                for ii in range(N_crates):
                    insert_list.append(stacks[from_bin].pop(0))
                stacks[to_bin] = insert_list + stacks[to_bin]

        tops = [stacks[key][0] for key in sorted(stacks.keys())]
        return "".join(tops)


    def create_line_generator(self):
            with open(self.input_file, 'r') as file:
                for line in file:
                    try:
                        yield line.replace('\n', '')
                    except ValueError as e:
                        print(f"Error returning line '{line.strip()}'")


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file = Path("inputs") / (stem + ".txt")

    DaySolver = Advent(input_file)

    print(f"Part 1: {DaySolver.sol1}")
    print(f"Part 2: {DaySolver.sol2}")

