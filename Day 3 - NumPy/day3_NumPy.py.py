import numpy as np

# Create NumPy Arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 4, 3, 2, 1])

print("Array 1:", array1)
print("Array 2:", array2)

# Addition
print("\nAddition:")
print(array1 + array2)

# Subtraction
print("\nSubtraction:")
print(array1 - array2)

# Multiplication
print("\nMultiplication:")
print(array1 * array2)

# Division
print("\nDivision:")
print(array1 / array2)

# Square each element
print("\nSquare of Array 1:")
print(array1 ** 2)

# Mean
print("\nMean of Array 1:")
print(np.mean(array1))

# Maximum
print("\nMaximum value:")
print(np.max(array1))

# Minimum
print("\nMinimum value:")
print(np.min(array1))

# Sum
print("\nSum of Array 1:")
print(np.sum(array1))