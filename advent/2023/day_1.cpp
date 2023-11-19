#include <iostream>
#include <fstream>
#include <string>
#include <cctype> // for std::isspace

bool isBlank(const std::string& line) {
	for (char ch : line) {
		if (!std::isspace(ch)) {
			return false; // The line is not blank
		}
	}
	return true; // The line is blank
}

int convertToInt(const std::string& input) {
	// Convert the line to an integer using std::stoi
    try {
        return std::stoi(line);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid input. Please enter a valid integer." << std::endl;
    } catch (const std::out_of_range& e) {
        std::cerr << "Input out of range for int." << std::endl;
    }

int main() {
    // Open the file
    std::ifstream inputFile("inputs/day_1.txt");

    // Check if the file is opened successfully
    if (!inputFile.is_open()) {
        std::cerr << "Error opening the file!" << std::endl;
        return 1; // Return an error code
    }


    // Read the file line by line
    std::string line;
	int blankLineCount = 0; // Counter for blank lines
   	int currentSum = 0; // Counter for sum of current list
	int maxSum = 0; // Sum of maximum 
	
	while (std::getline(inputFile, line)) {
        // Process each line as needed
	// Check if line is blank
		if (isBlank(line)) {
			if (maxSum	 #### TODO RESTART HERE

			std::cout << "BLANK" << std::endl;
			} else {
				currentSum +
			}
	}

	// Display the number of blank lines
	std::cout << "Number of blank lines: " << blankLineCount << std::endl;

    // Close the file
    inputFile.close();

    return 0; // Return 0 to indicate successful execution
}

