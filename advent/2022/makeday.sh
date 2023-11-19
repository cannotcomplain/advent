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
template_file="day_template.py"
output_file="day_${N}.py"

# Check if the output file already exists
if [ -e "$output_file" ]; then
    echo "Error: The file $output_file already exists. Choose a different value for N."
    exit 1
fi

# Copy the template file to the new file
cp "$template_file" "$output_file"

# Make the new file executable
chmod +x "$output_file"

echo "File $output_file created and made executable."
