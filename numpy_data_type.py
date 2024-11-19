import numpy as np
"""
NumPy supports several data types that you can use to create arrays. Here are the most commonly used NumPy data types:

1. Integer types
int8: 8-bit signed integer (-128 to 127)
int16: 16-bit signed integer (-32,768 to 32,767)
int32: 32-bit signed integer (-2,147,483,648 to 2,147,483,647)
int64: 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
uint8: 8-bit unsigned integer (0 to 255)
uint16: 16-bit unsigned integer (0 to 65,535)
uint32: 32-bit unsigned integer (0 to 4,294,967,295)
uint64: 64-bit unsigned integer (0 to 18,446,744,073,709,551,615)

2. Floating-point types
float16: Half precision float (16-bit)
float32: Single precision float (32-bit)
float64: Double precision float (64-bit) — Default for NumPy arrays

3. Complex types
complex64: Complex number with 32-bit real and imaginary parts
complex128: Complex number with 64-bit real and imaginary parts

4. Boolean type
bool: Boolean type (True or False)

5. String types
str_: String (fixed-length)
unicode_: Unicode string (fixed-length)

6. Object type
object: Generic object type (can be any Python object)

7. Datetime types
datetime64: Date and time
timedelta64: Time difference

8. Other types
void: Used for arbitrary (raw) data. Useful for structured data types.
"""

""""
Focus on these key data types first:
int32, int64 - Common for integer arrays.
float32, float64 - Used for arrays of floating-point numbers. float64 is the default.
bool - Useful for Boolean arrays (True/False).
object - Used for arrays containing any type of Python objects.
datetime64 - For date and time data (useful for time series analysis).
You can refer to the others as needed:
complex types (complex64, complex128) are useful for scientific computing.
string types (str_, unicode_) are not used as much in numerical computations but can be 
important in text data processing.
"""
# Integer
int_arr = np.array([1, 2, 3], dtype=np.int32)
print(int_arr.dtype)  # Output: int32

# Float
float_arr = np.array([1.1, 2.2, 3.3], dtype=np.float64)
print(float_arr.dtype)  # Output: float64

# Complex
complex_arr = np.array([1+2j, 3+4j], dtype=np.complex128)
print(complex_arr.dtype)  # Output: complex128

# Boolean
bool_arr = np.array([True, False, True], dtype=np.bool_)
print(bool_arr.dtype)  # Output: bool_

# String
str_arr = np.array(["apple", "banana", "cherry"], dtype=np.str_)
print(str_arr.dtype)  # Output: <U6
