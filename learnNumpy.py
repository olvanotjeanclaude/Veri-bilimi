# NumPy Cheatsheet
import numpy as np
import platform
import pandas as pd

# NumPy Data Types with Descriptions and Examples

data_types = {
    'int8': {'type_code': 'i1', 'description': 'Signed 8-bit integer', 'example': "-128 to 127"},
    'uint8': {'type_code': 'u1', 'description': 'Unsigned 8-bit integer', 'example': "0 to 255"},
    'int16': {'type_code': 'i2', 'description': 'Signed 16-bit integer', 'example': "-32,768 to 32,767"},
    'uint16': {'type_code': 'u2', 'description': 'Unsigned 16-bit integer', 'example': "0 to 65,535"},
    'int32': {'type_code': 'i4', 'description': 'Signed 32-bit integer', 'example': "-2,147,483,648 to 2,147,483,647"},
    'uint32': {'type_code': 'u4', 'description': 'Unsigned 32-bit integer', 'example': "0 to 4,294,967,295"},
    'int64': {'type_code': 'i8', 'description': 'Signed 64-bit integer', 'example': "-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807"},
    'uint64': {'type_code': 'u8', 'description': 'Unsigned 64-bit integer', 'example': "0 to 18,446,744,073,709,551,615"},
    'float16': {'type_code': 'f2', 'description': '16-bit floating point', 'example': "±65504 (floating point precision)"},
    'float32': {'type_code': 'f4', 'description': '32-bit floating point', 'example': "±3.4 × 10^38 (floating point precision)"},
    'float64': {'type_code': 'f8', 'description': '64-bit floating point', 'example': "±1.8 × 10^308 (floating point precision)"},
    'float128': {'type_code': 'f16', 'description': '128-bit floating point', 'example': "Very high precision floating point (rarely used)"},
    'complex64': {'type_code': 'c8', 'description': 'Complex number with 64-bit real and imaginary parts', 'example': "Real and Imaginary part each using float32"},
    'complex128': {'type_code': 'c16', 'description': 'Complex number with 128-bit real and imaginary parts', 'example': "Real and Imaginary part each using float64"},
    'bool': {'type_code': '', 'description': 'Boolean type (True or False)', 'example': "True or False"},
    'object': {'type_code': 'O', 'description': 'Object (can be any Python object)', 'example': "Any Python object, e.g. list, dictionary, function"},
    'string_': {'type_code': 'S', 'description': 'Fixed-size string (not Unicode)', 'example': "'hello' (for 5 characters)"},
    'unicode_': {'type_code': 'U', 'description': 'Unicode string', 'example': "'你好' (Chinese characters)"},
}

# print(data_types['int32'])

# print('Python version: ' + platform.python_version())
# print('Numpy version: ' + np.__version__)

arr = np.array([1,2,3])
# print(arr)
# print(arr.dtype)# Creating a NumPy array with string data type
arr = np.array(['hello', 'world', 'hi'], dtype='S5')  # S5 means fixed size 5 for each string

print(arr)  # Output: [b'hello' b'world' b'hi   ']

arr = np.array([1+2j, 3-4j], dtype='c8')
print(arr)
print(arr.dtype)


arr = np.array([0, 1, 2], dtype="bool")
print(arr)
print(arr.dtype)

# 1. Creating Arrays
arr1 = np.array([1, 2, 3])                     # 1D array
arr2 = np.array([[1, 2], [3, 4]])             # 2D array
zeros = np.zeros((3,3))                      # 3x3 array of zeros
print(zeros)
ones = np.ones((2, 2))                        # 2x2 array of ones
identity = np.eye(3)                          # 3x3 identity matrix
full = np.full((2, 3), 7)                     # 2x3 array filled with 7
arange = np.arange(0, 10, 2)                  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)               # [0, 0.25, 0.5, 0.75, 1]

# np.linspace(start, stop, num_of_elements, endpoint=True, retstep=False) 
arr = np.linspace(0, 3, 4,endpoint=True, retstep=False)

# 2. Array Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sum_arr = a + b                               # Element-wise addition
diff_arr = a - b                              # Element-wise subtraction
prod_arr = a * b                              # Element-wise multiplication
div_arr = b / a                               # Element-wise division
scalar_add = a + 10                           # Scalar addition
scalar_mult = b * 2                           # Scalar multiplication
sqrt_arr = np.sqrt(a)                         # Square root
log_arr = np.log(a)                           # Natural logarithm

# 3. Indexing and Slicing
c = np.array([[1, 2, 3], [4, 5, 6]])
elem = c[0, 1]                                # Access single element
row = c[1, :]                                 # Slice row
col = c[:, 2]                                 # Slice column
sub_matrix = c[0:2, 1:3]                     # Slice sub-matrix

# 4. Aggregations
d = np.array([1, 2, 3, 4])
total = np.sum(d)                             # Sum of elements
mean = np.mean(d)                             # Mean
std = np.std(d)                               # Standard deviation
min_val = np.min(d)                           # Minimum
max_val = np.max(d)                           # Maximum

# 5. Reshaping and Transposing
e = np.array([1, 2, 3, 4, 5, 6])
reshaped = e.reshape(2, 3)                    # Reshape to 2x3
transposed = reshaped.T                       # Transpose

# 6. Random Numbers
random_array = np.random.rand(3, 3)           # Random array in [0, 1)
random_ints = np.random.randint(1, 10, (2, 2))# Random integers in [1, 10)

# 7. Stacking Arrays
f = np.array([1, 2])
g = np.array([3, 4])
stacked = np.vstack((f, g))                   # Vertical stack
hstacked = np.hstack((f, g))                  # Horizontal stack

