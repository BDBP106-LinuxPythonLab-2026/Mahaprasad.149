import time


# Custom decorator to calculate execution time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print("\nTime taken for matrix multiplication:",
              end_time - start_time, "seconds")

        return result

    return wrapper


class LinearAlgebra:

    def __init__(self):
        self._A = []
        self._B = []

        # Get matrix A
        print("Enter dimensions of Matrix A:")
        rows_A = int(input("Number of rows: "))
        cols_A = int(input("Number of columns: "))

        self._A = self.input_matrix(rows_A, cols_A, "A")

        # Get matrix B
        print("\nEnter dimensions of Matrix B:")
        rows_B = int(input("Number of rows: "))
        cols_B = int(input("Number of columns: "))

        self._B = self.input_matrix(rows_B, cols_B, "B")

    # Function to accept matrix elements
    def input_matrix(self, rows, cols, name):
        matrix = []

        print(f"\nEnter elements of Matrix {name}:")

        for i in range(rows):
            row = []

            for j in range(cols):
                element = float(
                    input(f"Enter element [{i+1}][{j+1}]: ")
                )
                row.append(element)

            matrix.append(row)

        return matrix

    # Property decorator to access matrices A and B
    @property
    def matrices(self):
        return self._A, self._B

    # Setter to modify matrices A and B
    @matrices.setter
    def matrices(self, new_matrices):

        A, B = new_matrices

        if not A or not B:
            raise ValueError("Matrices cannot be empty.")

        if any(len(row) != len(A[0]) for row in A):
            raise ValueError("Matrix A has inconsistent row lengths.")

        if any(len(row) != len(B[0]) for row in B):
            raise ValueError("Matrix B has inconsistent row lengths.")

        if len(A[0]) != len(B):
            raise ValueError(
                "Matrix multiplication is not possible. "
                "Columns of A must equal rows of B."
            )

        self._A = A
        self._B = B

    # Instance method for matrix multiplication
    @calculate_time
    def multiply(self):

        A = self._A
        B = self._B

        rows_A = len(A)
        cols_A = len(A[0])

        rows_B = len(B)
        cols_B = len(B[0])

        # Check multiplication condition
        if cols_A != rows_B:
            raise ValueError(
                "Matrix multiplication is not possible!"
                " Columns of A must equal rows of B."
            )

        # Initialize result matrix with zeros
        result = [
            [0 for j in range(cols_B)]
            for i in range(rows_A)
        ]

        # Perform matrix multiplication
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    result[i][j] += A[i][k] * B[k][j]

        return result


# Main program
try:

    obj = LinearAlgebra()

    # Access matrices using property
    A, B = obj.matrices

    print("\n Matrix A:")
    for row in A:
        print(row)

    print("\n Matrix B:")
    for row in B:
        print(row)

    # Perform multiplication
    result = obj.multiply()

    print("\n Result of Matrix Multiplication:")
    for row in result:
        print(row)

    # Modify matrices if required
    choice = input("\n Do you want to modify matrices? (yes/no): ")

    if choice.lower() == "yes":

        print("\n Enter new matrices:")

        new_A = obj.input_matrix(
            int(input("Rows of A: ")),
            int(input("Columns of A: ")),
            "A"
        )

        new_B = obj.input_matrix(
            int(input("Rows of B: ")),
            int(input("Columns of B: ")),
            "B"
        )

        # Update matrices using setter
        obj.matrices = (new_A, new_B)

        print("\n Updated Matrix A:", obj.matrices[0])
        print("Updated Matrix B:", obj.matrices[1])

        # Multiply updated matrices
        result = obj.multiply()

        print("\n Updated multiplication result:")
        for row in result:
            print(row)

except ValueError as e:
    print("\n Error:", e)