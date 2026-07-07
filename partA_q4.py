# ==========================================
# Question 4: Vectorized Operations
# ==========================================

import numpy as np
import time

print("\n========== VECTORIZED OPERATIONS ==========")

# ------------------------------
# Traditional Loop
# ------------------------------

numbers = [10, 20, 30, 40, 50]

start = time.time()

result = []

for num in numbers:
    result.append(num + 10)

end = time.time()

print("\nTraditional Loop Result:")
print(result)

print("Time Taken:", end - start)


# ------------------------------
# NumPy Vectorized Operation
# ------------------------------

numbers_np = np.array([10, 20, 30, 40, 50])

start = time.time()

result_np = numbers_np + 10

end = time.time()

print("\nVectorized Operation Result:")
print(result_np)

print("Time Taken:", end - start)


# ------------------------------
# Vectorized Example
# ------------------------------

print("\nOriginal Array:")
print(numbers_np)

print("\nMultiply by 5:")
print(numbers_np * 5)

print("\nSquare of each element:")
print(numbers_np ** 2)

print("\nSquare Root:")
print(np.sqrt(numbers_np))