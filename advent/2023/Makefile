CXX := g++
CXXFLAGS := -std=c++11 -Wall -Wextra

SRC := $(wildcard day_*.cpp)
OBJ := $(SRC:.cpp=.o)
EXECUTABLE := my_program

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJ)
	$(CXX) $(CXXFLAGS) $(OBJ) -o $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXECUTABLE)

# Target-specific rules for individual days
day_%: day_%.o
	$(CXX) $(CXXFLAGS) $< -o $@_executable

