import numpy as np

# 1. Creating Arrays
arr = np.array([1, 2, 3, 4, 5])  # 1D Array
arr_2d = np.array([[1, 2], [3, 4], [5, 6]])  # 2D Array
zeros_arr = np.zeros((3, 3))  # Zeros Array
ones_arr = np.ones((2, 3))  # Ones Array
identity_matrix = np.eye(4)  # Identity Matrix
linspace_arr = np.linspace(0, 10, 5)  # Linspace Array
random_arr = np.random.rand(3, 2)  # Random Array (uniform)
random_int_arr = np.random.randint(0, 10, (3, 2))  # Random Integer Array

# 2. Array Properties
shape = arr.shape  # Shape of Array
dims = arr.ndim  # Dimensions of Array
size = arr.size  # Size of Array
dtype = arr.dtype  # Data Type of Array
itemsize = arr.itemsize  # Item Size (bytes) of Array

# 3. Array Indexing & Slicing
first_element = arr[0]  # First element of 1D Array
element_2d = arr_2d[1, 1]  # Element at [1,1] in 2D Array
first_two_elements = arr[:2]  # First two elements of 1D Array
slice_2d = arr_2d[1:, 1:]  # Slice from second row and second column in 2D Array
last_element = arr[-1]  # Last element of 1D Array
every_second_element = arr[::2]  # Every second element of 1D Array

############### Indexing and Slicing ##############################
# Indexing in 1D Array
arr = np.array([10, 20, 30, 40, 50])

# Access the first element
arr[0]  # 10

# Access the last element
arr[-1]  # 50

# Access the second element
arr[1]  # 20

# Indexing in 2D Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access element in the first row, second column
arr_2d[0, 1]  # 2

# Access element in the second row, third column
arr_2d[1, 2]  # 6

# Accessing entire row
arr_2d[0]  # [1 2 3]

# Accessing entire column
arr_2d[:, 1]  # [2 5 8]

# Slicing in 1D Array
arr[1:4]  # [20 30 40]
arr[:3]   # [10 20 30]
arr[2:]   # [30 40 50]
print("***")
print(arr)
# Slicing in 2D Array
arr_2d[:2, 1:3]  # [[2 3], [5 6]]

# Slice entire first column
arr_2d[:, 0]  # [1 4 7]

# Slicing with Step
arr[::2]  # [10 30 50]

# Negative Indexing
arr[-1]  # 50
arr[-2:]  # [40 50]

# Advanced Slicing
arr_2d[-2:, :2]  # [[4 5], [7 8]]
arr_2d[:2, 1:3]  # [[2 3], [5 6]]
############### Indexing and Slicing ##############################

# 4. Array Operations
add_10 = arr + 10  # Add 10 to each element of Array
sub_5 = arr - 5  # Subtract 5 from each element of Array
multiply_2 = arr * 2  # Multiply each element by 2
divide_2 = arr / 2  # Divide each element by 2
square_elements = arr ** 2  # Square each element of Array
arr_sum = arr.sum()  # Sum of all elements
sum_columns = arr_2d.sum(axis=0)  # Sum along columns in 2D Array
sum_rows = arr_2d.sum(axis=1)  # Sum along rows in 2D Array
mean = arr.mean()  # Mean of Array
min_value = arr.min()  # Minimum value in Array
max_value = arr.max()  # Maximum value in Array
min_index = arr.argmin()  # Index of minimum value in Array
max_index = arr.argmax()  # Index of maximum value in Array
std_dev = arr.std()  # Standard Deviation of Array

# Original 1D array with 6 elements
arr = np.array([10, 20, 30, 40, 50, 60])

# Reshape the array into a 2x3 shape
reshaped = arr.reshape((2, 3))  # Reshape Array
print(reshaped)  # [[10 20 30]
                 #  [40 50 60]]

transposed = arr_2d.T  # Transpose of 2D Array

# 5. Broadcasting
arr1 = np.array([1, 2, 3])  # 1D Array
arr2 = np.array([[1], [2], [3]])  # 2D Array (column vector)
broadcasted = arr1 + arr2  # Broadcasting addition of two arrays

# 6. Stacking and Splitting Arrays
vstack_arr = np.vstack([arr1, arr2.flatten()])  # Vertical stacking
hstack_arr = np.hstack([arr1, arr2.flatten()])  # Horizontal stacking
split_arr = np.split(arr, 3)  # Split array into 3 parts

# 7. Mathematical Functions
add_arrays = np.add(arr, arr)  # Add two arrays
subtract_arrays = np.subtract(arr, arr)  # Subtract arrays
multiply_arrays = np.multiply(arr, arr)  # Multiply arrays
divide_arrays = np.divide(arr, arr)  # Divide arrays
exp = np.power(arr, 2)  # Exponentiate array

# 8. Random Numbers
random_float = np.random.rand(2, 3)  # Random float between 0 and 1
random_ints = np.random.randint(1, 10, (2, 3))  # Random integers between 1 and 10
random_normal = np.random.randn(3, 2)  # Random normal distribution
random_choice = np.random.choice([1, 2, 3, 4])  # Random choice from a list

# 9. Linear Algebra
A = np.array([[1, 2], [3, 4]])  # Matrix A
B = np.array([[5], [6]])  # Matrix B
dot_product = np.dot(A, B)  # Dot product of matrices
matrix_multiply = np.matmul(A, B)  # Matrix multiplication
det_A = np.linalg.det(A)  # Determinant of matrix A
eigenvalues, eigenvectors = np.linalg.eig(A)  # Eigenvalues and Eigenvectors

# 10. String Operations
str_arr = np.array(['apple', 'banana', 'cherry'])  # String array
str_lengths = np.char.str_len(str_arr)  # String lengths
upper_str = np.char.upper(str_arr)  # Convert strings to uppercase
replaced_str = np.char.replace(str_arr, 'a', 'o')  # Replace 'a' with 'o' in strings

# 11. Array Comparison
arr1_equal_arr2 = np.equal(arr1, arr2)  # Compare if arrays are equal element-wise
arr1_less_than_arr2 = np.less(arr1, arr2)  # Compare if elements in arr1 are less than those in arr2
arr1_greater_than_arr2 = np.greater(arr1, arr2)  # Compare if elements in arr1 are greater than those in arr2

p = np.full_like([0,3], 7)
print(p)