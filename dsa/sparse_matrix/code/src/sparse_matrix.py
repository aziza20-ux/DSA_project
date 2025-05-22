class SparseMatrix():
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

        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip() != '']
        except FileNotFoundError:
            raise FileNotFoundError("file {file_path} doesn't exist")
        n_rows = int(lines[0].split('=')[1])
        n_cols = int(lines[1].split('=')[1])

        matrix = cls(n_rows, n_cols)
        for line in lines[2:]:
            if not (line.startswith('(') and line.endswith(')')):
                raise ValueError("this sparsematrix doen't follow the format")
            try:
                line = line.strip()[1:-1]
                row, col, value = line.split(',')
                row, col, value = int(row), int(col), int(value)

                matrix.setElements(row, col, value)
            except Exception:
                raise ValueError ("wrong format input")
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

    def write_to_file(self, file_path):

        try:
            with open(file_path, 'w') as f:
                f.write(f"rows={self.n_rows}\n")
                f.write(f"cols={self.n_cols}\n")
                for (row, col), v in sorted(self.data.items()):
                    f.write(f"({row}, {col}, {v})\n")
        except Exception:
            raise ValueError("no file found please provide one")


def main():

    print("play with these operations\n")
    print("choose among these operations: add/substract/multiply")
    choice = input("enter your choice\n").strip().lower()

    fil1 = input("enter the first matrix file path\n").strip()
    fil2 = input("enter the second matrix file path\n").strip()

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

        print("successfull!!", result_file)

    except Exception as e:
        print("ERROR:", e)


if __name__ == '__main__':
    main()
