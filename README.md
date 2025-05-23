Sparse Matrix Operations
📌 Overview
This project implements a custom SparseMatrix class in Python to efficiently handle and perform operations on large sparse matrices. Sparse matrices are those in which most of the elements are zero, and this implementation saves memory by only storing non-zero elements in a dictionary.

The program supports:

Loading sparse matrices from a file

Matrix addition

Matrix subtraction

Matrix multiplication

Writing results to a file

This is a solution to a programming assignment under the course Data Structures and Algorithms for Engineers.

🧠 Key Features
Efficient Storage: Only non-zero values are stored to optimize memory usage.

Matrix Operations: Supports addition, subtraction, and multiplication.

File I/O: Load matrix data from a file and export results back to a file.

User Interaction: Interactive command-line interface to perform operations.

🗂️ Project Structure
css
Copy
Edit
/dsa/sparse_matrix/
│
├── code/
│   └── src/
│       └── sparse_matrix.py      # Main source code file
│
└── sample_inputs/
    └── matrixA.txt               # Sample input matrix A
    └── matrixB.txt               # Sample input matrix B
🧾 Input File Format
Each matrix input file must follow this format:

makefile
Copy
Edit
rows=8433
cols=3180
(0, 381, -694)
(0, 128, -838)
...
rows and cols specify the dimensions of the matrix.

Each non-zero element is defined as a tuple (row, column, value).

All unspecified elements are assumed to be zero.

🚀 How to Use
Ensure your matrix files follow the correct format.

Run the script:

bash
Copy
Edit
python sparse_matrix.py
Follow the prompts to:

Select an operation (add, substract, multiply)

Enter the paths to the input files

Provide a path to save the result

🔐 Error Handling
The program handles:

File not found errors

Incorrectly formatted files

Invalid operations (e.g., mismatched matrix dimensions)

Non-integer or floating-point values in the input

🔧 Class & Method Documentation
class SparseMatrix
A class that represents a sparse matrix using a dictionary.

__init__(self, n_rows, n_cols)
Initializes the matrix with dimensions n_rows x n_cols.

setElements(row, col, value)
Sets a value at the given position. Zero values are not stored.

getElements(row, col)
Returns the value at the specified position. Defaults to 0 if not set.

load_from_file(file_path)
Loads matrix data from a file and returns a SparseMatrix object.

write_to_file(file_path)
Writes the matrix data to a file in the specified format.

add(matrix_B)
Returns a new SparseMatrix that is the result of adding the current matrix with matrix_B.

substract(matrix_B)
Returns a new SparseMatrix that is the result of subtracting matrix_B from the current matrix.

multiply(matrix_B)
Returns a new SparseMatrix that is the result of multiplying the current matrix with matrix_B.

🧪 Sample Execution
text
Copy
Edit
play with these operations

choose among these operations: add/substract/multiply
enter your choice
add
enter the first matrix file path
sample_inputs/matrixA.txt
enter the second matrix file path
sample_inputs/matrixB.txt
enter a file path where to see your result: output.txt
successfull!! check your results in this file path : output.txt

👨‍🏫 Author & License
Created by Aziza as part of the course assignment for Data Structures and Algorithms for Engineers.
