
# Question 2: Array Indexing, Slicing,
# Reshaping and Mathematical Operations


import numpy as np

# Creating a 1D array
arr = np.array([10, 20, 30, 40, 50])

print("\n========== ARRAY INDEXING ==========")
print("Original Array:", arr)

# Indexing
print("First Element:", arr[0])
print("Third Element:", arr[2])
print("Last Element:", arr[-1])


# Creating a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\n2D Array:")
print(matrix)

# Indexing in 2D array
print("Element at Row 2, Column 2:", matrix[1,1])
print("Element at Row 3, Column 3:", matrix[2,2])


# ==========================================
# ARRAY SLICING
# ==========================================

print("\n========== ARRAY SLICING ==========")

print("Original Array:", arr)

print("Elements from index 1 to 3:", arr[1:4])

print("First Three Elements:", arr[:3])

print("Last Three Elements:", arr[2:])

print("Every Second Element:", arr[::2])


print("\n2D Array Slicing")

print("First Row:")
print(matrix[0,:])

print("Second Column:")
print(matrix[:,1])

print("First Two Rows:")
print(matrix[:2])


# ==========================================
# ARRAY RESHAPING
# ==========================================

print("\n========== ARRAY RESHAPING ==========")

numbers = np.arange(1,13)

print("Original Array:")
print(numbers)

reshape1 = numbers.reshape(3,4)

print("\nReshaped into 3 x 4:")
print(reshape1)

reshape2 = numbers.reshape(2,6)

print("\nReshaped into 2 x 6:")
print(reshape2)


# ==========================================
# MATHEMATICAL OPERATIONS
# ==========================================

print("\n========== MATHEMATICAL OPERATIONS ==========")

a = np.array([10,20,30])
b = np.array([1,2,3])

print("Array A:", a)
print("Array B:", b)

# Addition
print("\nAddition:")
print(a + b)

# Subtraction
print("\nSubtraction:")
print(a - b)

# Multiplication
print("\nMultiplication:")
print(a * b)

# Division
print("\nDivision:")
print(a / b)

# Power
print("\nSquare:")
print(a ** 2)

# Square Root
print("\nSquare Root:")
print(np.sqrt(a))

# Sum
print("\nSum of Elements:")
print(np.sum(a))

# Mean
print("\nAverage:")
print(np.mean(a))

# Maximum
print("\nMaximum Value:")
print(np.max(a))

# Minimum
print("\nMinimum Value:")
print(np.min(a))