import numpy as np
import pandas as pd

#zero matrix
zero_matrix = np.zeros((3, 4))  # Create a 3x4 matrix filled with zeros
print("Zero Matrix:\n", zero_matrix)  # Print the zero matrix

#ones matrix
ones_matrix = np.ones((2, 5))  # Create a 2x5 matrix filled with ones
print("Ones Matrix:\n", ones_matrix)  # Print the ones matrix

#identity matrix
identity_matrix = np.identity(4)  # Create a 4x4 identity matrix
print("Identity Matrix:\n", identity_matrix)  # Print the identity matrix

#diagonal matrix
diagonal_matrix = np.diag([1, 2, 3, 4])  # Create a diagonal matrix with the specified diagonal values
print("Diagonal Matrix:\n", diagonal_matrix)  # Print the diagonal matrix

#scalar matrix
scalar_matrix = np.full((3, 3), 5)  # Create a 3x3 matrix filled with the scalar value 5
for (row, column), value in np.ndenumerate(scalar_matrix):  # Iterate over the scalar matrix and print the index and value of each element
    if row != column:
        scalar_matrix[row,column] = 0  # Set the off-diagonal elements to zero
print("Scalar Matrix:\n", scalar_matrix)  # Print the scalar matrix

#random integer matrix
random_integer_matrix = np.random.randint(1, 11, size=(3, 4))  # Create a 3x4 matrix filled with random integers between 1 and 10
print("Random Integer Matrix:\n", random_integer_matrix)  # Print the random integer matrix

#determinant of a matrix
matrix = np.array([[1, 2], [3, 4]])  # Create a 2x2 matrix
determinant = np.linalg.det(matrix)  # Calculate the determinant of the matrix
print("Determinant of the Matrix:\n", determinant)  #Print the determinant of the matrix

