# ==========================================
# Question 3: Broadcasting
# ==========================================

import numpy as np

print("\n========== BROADCASTING ==========")

# Example 1: Adding a scalar to an array

arr = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(arr)

print("\nAdding 5 to every element:")
print(arr + 5)


# Example 2: Multiplying every element

print("\nMultiplying every element by 2:")
print(arr * 2)


# Example 3: Broadcasting with two arrays

array1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array2 = np.array([10, 20, 30])

print("\nFirst Array:")
print(array1)

print("\nSecond Array:")
print(array2)

print("\nBroadcasting Result:")
print(array1 + array2)

# Advantages of Broadcasting:
# 1. Eliminates the need for loops.
# 2. Makes code shorter and easier to read.
# 3. Improves performance because NumPy operations are optimized.
# 4. Uses memory efficiently by avoiding unnecessary copies of data.
# 5. Simplifies mathematical operations on arrays of different shapes.