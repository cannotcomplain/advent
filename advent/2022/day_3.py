#!/usr/bin/env python3

import os
import ipdb
from pathlib import Path
from typing import List, Union

""" Day 3

One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

Example:
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""

class Advent:
    def __init__(self, input_file: str | os.PathLike ):
        """Initialize the file path and create a generator to read in the input file"""

        self.input_file = input_file
        self.priority_list = 'abcdefghijklmnopqrstuvwxyz'
        self.priority_mapping = {char: idx+1 for idx, char in enumerate(self.priority_list)}

        # Run part 1
        self.sol1 = self.part1()
        # Run part 2
        self.sol2 = self.part2()

    def part1(self):
        """Part 1 solver."""


        pack_priorities = 0
        line_generator = self.create_line_generator()
        for line in line_generator:
            pockets = line[:len(line)//2], line[len(line)//2:]

            # using set() + union() to
            # Union Operation in two Strings
            res = set(pockets[0]).intersection(pockets[1])
            if len(res) > 1:
                print(f"Potential error. More than 1 element in both halves...{line}")
            res = list(res)[0]
#            if res is lowercase, low priority, otherwise high
            case_scale = 0 if res in self.priority_list else 26

            priority_score = self.priority_mapping[res.lower()] + case_scale
            pack_priorities += priority_score

        return pack_priorities


    def part2(self):
        """Part 2 solver."""

        summed_priorities = 0
        elf_group = []

        line_generator = self.create_line_generator()
        for idx, line in enumerate(line_generator):
            if (idx + 1) % 3 == 0:
                res = list(set(elf_group[0]).intersection(elf_group[1]).intersection(line))[0]
                case_scale = 0 if res in self.priority_list else 26
                priority_score = self.priority_mapping[res.lower()] + case_scale
                summed_priorities += priority_score
                elf_group = []
            else:
                elf_group.append(line)

        return summed_priorities

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

