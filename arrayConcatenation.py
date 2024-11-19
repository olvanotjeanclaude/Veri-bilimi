
# List Concatenation Methods:

# 1. Using the '+' operator:
# Combines two or more lists into a new list.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
result = lst1 + lst2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 2. Using the '+= ' operator (In-place Concatenation):
# Appends the elements of the second list to the first list.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1 += lst2
print(lst1)  # Output: [1, 2, 3, 4, 5, 6]

# 3. Using 'extend()' method:
# Adds all elements from the second list to the first list.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print(lst1)  # Output: [1, 2, 3, 4, 5, 6]

# 4. Using List Comprehension:
# Concatenate lists using a list comprehension (useful for combining and filtering).
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
result = [x for x in lst1] + [x for x in lst2]
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 5. Using 'itertools.chain()':
# Concatenates multiple iterables (not just lists) using itertools.
import itertools
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
result = list(itertools.chain(lst1, lst2))
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# 6. Using '*args' for multiple lists:
# Concatenate an arbitrary number of lists using *args in a function.
def concat_lists(*args):
    return [item for sublist in args for item in sublist]
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9]
result = concat_lists(lst1, lst2, lst3)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Key Differences Between Concatenation Methods:

# 1. '+' operator:
# - Combines two or more lists into a **new list**.
# - **Does not modify** the original lists.
# - Useful for simple concatenation.

# 2. '+= ' operator:
# - Appends the second list to the first list **in-place**.
# - **Modifies** the original list.
# - No return value (does not create a new list).

# 3. 'extend()' method:
# - Similar to '+=', but **more explicit**.
# - Adds all elements of the second list to the first list **in-place**.
# - **Modifies** the original list.

# 4. List Comprehension:
# - Creates a **new list** by concatenating lists, with the option to **filter** or **transform** the data during concatenation.
# - **Does not modify** the original lists.
# - More flexible, useful for transformations or filtering.

# 5. 'itertools.chain()':
# - Concatenates multiple iterables (lists, tuples, etc.) efficiently.
# - **Does not create intermediate lists**, making it memory efficient for large datasets.
# - **Returns a new iterable**, which can be converted to a list using `list()`.

# 6. '*args' in a function:
# - Concatenates an arbitrary number of lists passed as arguments to a function.
# - **Returns a new list** by iterating over each passed list.
# - Useful when dealing with multiple lists dynamically.

