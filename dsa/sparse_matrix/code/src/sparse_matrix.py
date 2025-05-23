
"""
this is class representation to save sparse matrix which has non-zeros
as means of saving memory.

1.`load_from_file`(the class constructor):
    this function as class constructor to build an instance
     here `matrix = cls(n_rows, n_cols)` from input files

2.`getElement():

    the method to retrieve a value from certain position
    to carry operation on it

3.`setElement()`:
    the method to save non-zero elements in dictionary
    and skip zeros as meaans of saving memory


4.`add`():
    the function which loops through keys of both matrices
    and add the value of position they have in common ans retain others
5.`substract`:
    the function which loops through keys of both matrices
    and substruct the value of position they have in common ans retain others
6.`multiply()`:
    this `multiply(self, matrix_B)` first checks if the columns of the first
    matrix is equal to the number of rows in the second matrix
    and loops through both matrices to
    maltiply each element on the first matrix column with the second's columns element
7.`write_to_file()`:
    the method to write the result of substraction, addition or multiplication
    of two matrices to a disered file also entered by a user
8.`main()`:
    the main function to get inputs from user
and print the results according to user's preferences


"""


class SparseMatrix():

    # the constructor of a class to
    # build matrix instance

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols

        self.data = {}

    def setElements(self, row, col, value):
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def getElements(self, row, col):
        return self.data.get((row, col), 0)

    @classmethod
    def load_from_file(cls, file_path):

        # this try block parses through matrix lines and remove whitespace, and
        # ignore empty lines
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip() != '']
        except FileNotFoundError:
            raise FileNotFoundError("file {file_path} doesn't exist")

        # this trims the number of rows and columns

        n_rows = int(lines[0].split('=')[1])
        n_cols = int(lines[1].split('=')[1])

        # creates an instance of `SparseMatrix` class

        matrix = cls(n_rows, n_cols)
        # loops through the lines to check if they folllow the format
        # and make a list of rows and columns matrix
        for line in lines[2:]:
            if not (line.startswith('(') and line.endswith(')')):
                raise ValueError("this sparsematrix doen't follow the format")
            try:
                line = line.strip()[1:-1]
                row, col, value = line.split(',')
                row, col, value = int(row), int(col), int(value)
                # adds the values to matrix
                matrix.setElements(row, col, value)
            except Exception:
                raise ValueError("wrong format input")
        return matrix

    def add(self, matrix_B):
        if self.n_rows != matrix_B.n_rows or self.n_cols != matrix_B.n_cols:
            raise ValueError("the dimensions of both are not the same")
        result = SparseMatrix(self.n_rows, self.n_cols)

        keys = set(self.data.keys()).union(set(matrix_B.data.keys()))

        for key in keys:
            val = self.getElements(*key) + matrix_B.getElements(*key)
            result.setElements(*key, val)
        return result

    def substract(self, matrix_B):
        if self.n_rows != matrix_B.n_rows or self.n_cols != matrix_B.n_cols:
            raise ("the dimensions of both are not the same")
        result = SparseMatrix(self.n_rows, self.n_cols)

        keys = set(self.data.keys()).union(set(matrix_B.data.keys()))

        for key in keys:
            val = self.getElements(*key) - matrix_B.getElements(*key)
            result.setElements(*key, val)
        return result

    def multiply(self, matrix_B):

          if self.n_cols != matrix_B.n_rows:


              raise ValueError("the columns of A is unequal to row")
          result = SparseMatrix(self.n_rows, matrix_B.n_cols)

          for (i, k), val in self.data.items():

             for j in range(matrix_B.n_cols):
                 val2 = matrix_B.getElements(k, j)
                 if val2 != 0:
                     curr = result.getElements(i, j)
                     result.setElements(i, j, curr + val * val2)
          return result

    #the method to write the result of substraction, addition or multiplication
    #of two matrices to a disered file also entered by a user"""

    def write_to_file(self, file_path):

        try:
            with open(file_path, 'w') as f:
                f.write(f"rows={self.n_rows}\n")
                f.write(f"cols={self.n_cols}\n")
                for (row, col), v in sorted(self.data.items()):
                    f.write(f"({row}, {col}, {v})\n")
        except Exception:
            raise ValueError("no file found please provide one")

#the main function to get inputs from user
#and print the results according to user's preferences
def main():

    print("play with these operations\n")
    print("choose among these operations: add/substract/multiply")
    choice = input("enter your choice:").strip().lower()

    fil1 = input("enter the first matrix file path:").strip()
    fil2 = input("enter the second matrix file path:").strip()

    A = SparseMatrix.load_from_file(fil1)
    B = SparseMatrix.load_from_file(fil2)

    try:
        if choice == "add":
            result = A.add(B)
        elif choice == "substract":
            result = A.substract(B)
        elif choice == "multiply":
            result = A.multiply(B)
        else:
            print("invalid operation\n")
            return

        result_file = input(
                "enter a file path where to see your result:").strip()
        result.write_to_file(result_file)

        print("successfull!! check your results here:", result_file)

    except Exception as e:
        print("ERROR:", e)


if __name__ == '__main__':
    main()
