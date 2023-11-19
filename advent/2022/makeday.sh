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
test_file="tests/template.py"
output_file="day_${N}.py"
input_file="inputs/day_${N}.txt"
test_output_file="tests/test_day_${N}.py"
test_input_file="tests/inputs/test_day_${N}.txt"

# Check if the output file already exists
if [ -e "$output_file" ]; then
    echo "Error: The file $output_file already exists. Choose a different value for N."
    exit 1
fi

if [ -e "$test_output_file" ]; then
    echo "Error: The file $test_output_file already exists. Choose a different value for N."
    exit 1
fi

# Copy the template file to the new file
cp "$template_file" "$output_file"
cp "$test_file" "$test_output_file"
touch "$input_file"
touch "$test_input_file"

# Prompt the user for the test output
#read -p "Day ${day_number}, Part 1 Test Output: " test_output

# Replace "<OUTPUT1>" with the user input in the new file
# sed -i "s|\"<OUTPUT1>\"|$test_output|g" "$test_output_file"
# Use awk to perform the replacement with double quotes
# # Use awk to perform the replacement with double quotes
#awk -v output="$test_output" '{gsub(/<OUTPUT1>/, "\"" output "\"")}1' "$new_file" > temp && mv temp "$new_file"


# Make the new file executable
chmod +x "$output_file"
chmod +x "$test_output_file"

echo "File $output_file created and made executable."
echo "File $test_output_file created and made executable."
echo "Add content to $input_file!"
echo "Add content to $test_input_file!"

vim -p "$test_input_file" "$test_output_file" "$input_file"
