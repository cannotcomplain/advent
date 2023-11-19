# test_day_template.py
import os
import pytest
import sys
from pathlib import Path

# Dynamically import the class based on the day number
def import_day_class(day_number):
    # Get the absolute path to the parent directory of the tests
    current_file = Path(__file__)
    parent_dir = current_file.parent.parent.absolute()
#   import ipdb; ipdb.set_trace()

    # Add the parent directory to the system path to enable import
    sys.path.append(parent_dir)

    module_name = f'day_{day_number}'
    class_name = 'Advent'

    module = __import__(module_name)

    # Remove the parent directory from the system path to avoid side effects
    sys.path.remove(parent_dir)

    return getattr(module, class_name)


@pytest.fixture
def day_instance(request):
    # Get the test file name (e.g., "test_day_3.py")
    test_file_name = Path(request.fspath).stem

    # Extract the day number from the test file name
    day_number = int(test_file_name.split("_")[2].split(".")[0])

    # Import the appropriate class based on the day number
    day_class = import_day_class(day_number)

#    # Get the absolute path to the parent directory of the tests
#    parent_dir = Path(__file__).resolve().parent.parent
#
#    # Construct the input file path based on the day number
#    input_file_path = parent_dir / f"day{day_number}_input.txt"
    input_file_path = Path(__file__).parent.joinpath("inputs/").joinpath(test_file_name + ".txt")

    # Return an instance of the class with the input file path
    return day_class(input_file_path)

def test_part1(day_instance):
    expected_output = 157
    # Assert that the result matches the expected output
    assert day_instance.sol1 == expected_output

def test_part2(day_instance):
    expected_output = 70

    # Assert that the result matches the expected output
    assert day_instance.sol2 == expected_output
