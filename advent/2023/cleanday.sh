#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <N>"
    exit 1
fi

# Get the value of N from the command line argument
N=$1

# Check if N is a positive integer
if ! [[ "$N" =~ ^[1-9][0-9]*$ ]]; then
    echo "Error: N should be a positive integer."
    exit 1
fi

# Define file names
output_file="day_${N}.py"
input_file="inputs/day_${N}.txt"
test_output_file="tests/test_day_${N}.py"
test_input_file="tests/inputs/test_day_${N}.txt"

# Check if the output file already exists
if [ -e "$output_file" ]; then
    echo "$output_file deleted."
    rm "$output_file"
fi
if [ -e "$input_file" ]; then
    echo "$input_file deleted."
    rm "$input_file"
fi
if [ -e "$test_output_file" ]; then
    echo "$test_output_file deleted."
    rm "$test_output_file"
fi
if [ -e "$test_input_file" ]; then
    echo "$test_input_file deleted."
    rm "$test_input_file"
fi

