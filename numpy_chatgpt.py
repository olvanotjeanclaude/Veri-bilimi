# ---------------------------- NumPy Full Cheatsheet ----------------------------

import numpy as np

# ---------------------------- 1. Creating Arrays ----------------------------

# From a list
arr = np.array([1, 2, 3, 4])

# Zeros and ones
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((2, 3))    # 2x3 array of ones

# Identity matrix
identity = np.eye(3)  # 3x3 identity matrix

# Range of numbers
arr_range = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Linearly spaced values
arr_linspace = np.linspace(0, 1, 5)  # 5 values between 0 and 1

# Random values (Uniform distribution between 0 and 1)
random_vals = np.random.rand(3,5)

# Random integers
random_ints = np.random.randint(0, 10, (2, 3))  # Random integers between 0 and 10
print(random_ints)
# ---------------------------- 2. Array Properties ----------------------------

# Shape and dimensions
print(arr.shape)  # Shape of the array
print(arr.ndim)   # Number of dimensions

# Size and item size
print(arr.size)      # Total number of elements
print(arr.itemsize)  # Size (in bytes) of each element

# ---------------------------- 3. Reshaping Arrays ----------------------------

reshaped_arr = np.reshape(arr, (2, 2))  # Reshape into 2x2 array

# Reshaping with -1 to infer shape
reshaped_arr2 = np.reshape(arr, (-1, 2))  # Automatically calculate number of rows

# ---------------------------- 4. Array Indexing and Slicing ----------------------------
arr = np.array([1, 2, 3, 4])
print(arr)

# Accessing elements
print(arr[0])  # First element
print(arr[1, 2])  # 2D array access (2nd row, 3rd column)

# Slicing arrays
print(arr[0:2])  # Elements from index 0 to 2
print(arr[:3])   # First 3 elements
print(arr[::2])  # Every second element

# Negative indexing
print(arr[-1])  # Last element

# 2D slicing
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[1, 2])  # Access last element of second row

# ---------------------------- 5. Array Operations ----------------------------

# Element-wise operations
print(arr + 2)   # Add 2 to each element
print(arr * 3)   # Multiply each element by 3
print(arr ** 2)  # Square each element

# Sum, Mean, etc.
print(arr.sum())  # Sum of all elements
print(arr.mean())  # Mean of all elements
print(arr.max())   # Maximum element
print(arr.min())   # Minimum element

# Axis operations (e.g., summing over rows or columns)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.sum(axis=0))  # Sum along columns (axis=0)
print(arr_2d.sum(axis=1))  # Sum along rows (axis=1)

# ---------------------------- 6. Advanced Array Operations ----------------------------

# Dot product
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.dot(arr1, arr2))  # Dot product of two arrays

# Matrix multiplication
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(np.matmul(arr1, arr2))  # Matrix multiplication

# Transpose
print(arr_2d.T)  # Transpose of the array

# Element-wise trigonometric functions
print(np.sin(arr))  # Sine of each element
print(np.cos(arr))  # Cosine of each element

# ---------------------------- 7. Broadcasting ----------------------------

# Broadcasting operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # Element-wise sum

# Broadcasting a scalar across an array
arr3 = np.array([[1, 2], [3, 4]])
print(arr3 + 5)  # Add 5 to each element of the array

# ---------------------------- 8. Array Concatenation and Stacking ----------------------------

# Concatenate
arr3 = np.array([7, 8, 9])
concat_arr = np.concatenate((arr, arr3))  # Concatenate arrays

# Stacking
stacked_arr = np.stack((arr, arr3), axis=0)  # Stack arrays along new axis (axis 0)
hstack_arr = np.hstack((arr, arr3))  # Stack arrays horizontally
vstack_arr = np.vstack((arr, arr3))  # Stack arrays vertically

# ---------------------------- 9. Array Split and Reshape ----------------------------

# Split arrays
split_arr = np.split(arr, 2)  # Split array into 2 parts

# Reshaping arrays
reshaped_arr_2 = arr.reshape((2, 2))  # Reshape the array to 2x2

# ---------------------------- 10. Random Module ----------------------------

# Random numbers
random_arr = np.random.rand(3, 2)  # Random numbers in [0, 1)
random_norm = np.random.randn(3, 2)  # Random numbers from normal distribution

# Random integers
random_int = np.random.randint(0, 10, (2, 3))  # Random integers between 0 and 10

# ---------------------------- 11. NumPy Data Types ----------------------------

# List of NumPy Data Types
print(np.int8)  # int8
print(np.uint8)  # uint8
print(np.float32)  # float32
print(np.complex128)  # complex128

# Example usage of some data types
arr_int8 = np.array([1, 2, 3], dtype=np.int8)
arr_float32 = np.array([1.5, 2.5, 3.5], dtype=np.float32)

# ---------------------------- 12. Other Useful Functions ----------------------------

# Unique elements
unique_elements = np.unique(arr)

# Sorting
sorted_arr = np.sort(arr)

# Find elements
index = np.where(arr == 3)  # Find index where value is 3

# ---------------------------- 13. String Operations ----------------------------

# Array of strings
str_arr = np.array(['a', 'b', 'c'])
uppercase_str_arr = np.char.upper(str_arr)  # Convert to uppercase
lowercase_str_arr = np.char.lower(str_arr)  # Convert to lowercase
str_length = np.char.str_len(str_arr)  # Length of each string

# ---------------------------- 14. Linear Algebra ----------------------------

# Determinant of a matrix
matrix = np.array([[1, 2], [3, 4]])
det = np.linalg.det(matrix)
print(f"Determinant of matrix: {det}")

# Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors: {eigenvectors}")

# Solving linear equations
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
solution = np.linalg.solve(A, b)
print(f"Solution to linear equations: {solution}")

# ---------------------------- 15. Polynomial Operations ----------------------------

# Polynomial fitting
coefficients = np.polyfit([1, 2, 3], [4, 5, 6], 1)
print(f"Polynomial coefficients: {coefficients}")

# ---------------------------- Conclusion ----------------------------

print("This cheatsheet covers basic to advanced operations in NumPy, including array creation, indexing, slicing, reshaping, broadcasting, random number generation, linear algebra, and more.")
