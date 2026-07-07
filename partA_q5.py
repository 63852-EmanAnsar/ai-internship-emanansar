# ==========================================
# Question 5: Linear Algebra Operations
# ==========================================

import numpy as np

print("\n========== LINEAR ALGEBRA OPERATIONS ==========")

# Create two matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# ==========================================
# 1. Dot Product
# ==========================================

print("\n1. Dot Product:")
dot_product = np.dot(matrix1, matrix2)
print(dot_product)

# ==========================================
# 2. Matrix Multiplication
# ==========================================

print("\n2. Matrix Multiplication:")
matrix_multiplication = np.matmul(matrix1, matrix2)
print(matrix_multiplication)

# Another way to perform matrix multiplication
print("\nMatrix Multiplication using @ operator:")
print(matrix1 @ matrix2)

# ==========================================
# 3. Transpose
# ==========================================

print("\n3. Transpose of Matrix 1:")
transpose = matrix1.T
print(transpose)

# ==========================================
# 4. Inverse
# ==========================================

print("\n4. Inverse of Matrix 1:")
inverse = np.linalg.inv(matrix1)
print(inverse)