#!/usr/bin/env python3

from pathlib import Path
from typing import List

def part1(input_file):

    calorie_count = 0
    max_calories = 0

    with open(input_file, 'r') as f:
        for line in f:
            if f is

    return 'not done'


def part2(input):


    return 'not done'


if __name__ == "__main__":
    stem: str = Path(__file__).stem
    input_file: Path = Path("input") / (stem + ".txt")
#    input: List[str] = input_file.read_text().splitlines()

    print(part1(input_file), part2(input_file))

