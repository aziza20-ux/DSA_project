
# Sparse Matrix Operations

This Python application is designed to efficiently handle **sparse matrices**, which are matrices primarily composed of zero values. The application supports reading matrices from files, performing arithmetic operations (addition, subtraction, multiplication), and writing the result to a file. It optimizes memory usage and computation by storing only non-zero elements.

## Features

- **Sparse Matrix Representation**: Uses a dictionary to store non-zero elements, significantly saving memory.
- **Load from File**: Read matrices from files with a specific format.
- **Matrix Operations**:
  - Addition
  - Subtraction
  - Multiplication
- **Write to File**: Save the resulting matrix in the defined sparse format.
- **Error Handling**: Handles various input errors, including malformed files and incompatible dimensions.
- **Command Line Interaction**: Choose operations and input/output files interactively.

## Technologies Used

- **Python 3**: Core programming language used.
- No external libraries are used; custom implementations are provided for matrix operations.

## File Format

The input file format must be as follows:

```
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
(0, 639, 857)
...
```

- First two lines specify dimensions.
- Remaining lines list non-zero entries as (row, col, value).

## Local Setup

### Clone the Repository

```
git clone <repository_url>
cd <repository_directory>
```

### Run the Program

Ensure Python 3 is installed, then execute:

```
python3 sparse_matrix.py
```

You will be prompted to enter:

- The operation (`add`, `substract`, or `multiply`)
- Paths to the input files for matrices A and B
- The output file path for the result

## Example Usage

1. Prepare two matrix files in the correct format.
2. Run the script and select an operation.
3. Provide the paths to both input files and the desired output file.
4. The result will be saved in the output file path you specify.

## Input File Variations Supported

- Whitespace lines are ignored.
- Errors are thrown for invalid formats (e.g., wrong brackets, floating points).

## Notes

- No built-in libraries (like `numpy` or `regex`) are used to demonstrate fundamental data structure handling.
- All operations are manually implemented to ensure full understanding and efficiency.

👨‍🏫 Author & License

Created by Aziza as part of the course assignment for Data Structures and Algorithms for Engineers.

