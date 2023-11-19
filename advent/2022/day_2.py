#!/usr/bin/env python3

import os
import ipdb
from pathlib import Path
from typing import List, Union, Literal


def my_choice_to_rps(choice: str):
    return {'X': 'rock',
            'Y': 'paper',
            'Z': 'scissors'}[choice.upper()]

def opponent_choice_to_rps(choice: str):
    return {'A': 'rock',
            'B': 'paper',
            'C': 'scissors'}[choice.upper()]

def play_rps(opponent_hand, my_hand):
    if my_hand == opponent_hand:
        score = 3 # tie
    elif (
          (my_hand == 'rock' and opponent_hand == 'paper') or
          (my_hand == 'scissors' and opponent_hand == 'rock') or
          (my_hand == 'paper' and opponent_hand == 'scissors')
        ):
        score = 0
    else:
        score = 6

    return score

def score_choice(choice):
    return {'rock': 1,
            'paper': 2,
            'scissors': 3}[choice]

def score_hand(opponent_hand, my_hand):
    play_score = play_rps(opponent_hand, my_hand)
    hand_score = score_choice(my_hand)
    return play_score + hand_score

# part 2
def result_to_hand(opponent_hand: str, result):
    # given the opponents key, what value loses
    losing_hands = {'rock': 'scissors',
                   'paper': 'rock',
                   'scissors': 'paper'}
    outcome = {
            'X': 'lose',
            'Y': 'tie',
            'Z': 'win',
            }[result]

    if outcome == 'tie':
       my_hand = opponent_hand
    elif outcome == 'lose':
        my_hand = losing_hands[opponent_hand]
    else:
        winning_hands = {val: key for key, val in losing_hands.items()}
        my_hand = winning_hands[opponent_hand]

    return my_hand


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

        my_score = 0
        line_generator = self.create_line_generator()
        for line in line_generator:
            opponent_choice, my_choice = line.split()
            my_hand = my_choice_to_rps(my_choice)
            opponent_hand = opponent_choice_to_rps(opponent_choice)

            my_score += score_hand(opponent_hand, my_hand)

        return my_score


    def part2(self):
        """Part 2 solver."""
        my_score = 0
        line_generator = self.create_line_generator()
        for line in line_generator:
            opponent_choice, result = line.split()
            opponent_hand = opponent_choice_to_rps(opponent_choice)
            my_hand = result_to_hand(opponent_hand, result)
            my_score += score_hand(opponent_hand, my_hand)

        return my_score


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

