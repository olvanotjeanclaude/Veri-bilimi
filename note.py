from math import sqrt #built-in fonksiyonlar, kütüphane import etme 
import os 
#  specify the data
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Dictionary with different Python data types as values
data_types_dict = {
    "integer": 5,                       # int: Whole number
    "float": 3.14,                      # float: Decimal number
    "complex": 2 + 3j,                  # complex: Complex number
    "string": "Hello, world!",          # str: String
    "list": [1, 2, 3, 'hello'],         # list: Ordered collection (mutable)
    "tuple": (1, 2, 3, 'hello'),        # tuple: Ordered collection (immutable)
    "range": range(5),                  # range: Sequence of numbers
    "dictionary": {"name": "John", "age": 30},  # dict: Key-value pairs
    "set": {1, 2, 3, 4},                # set: Unordered collection of unique items
    "frozenset": frozenset([1, 2, 3]),  # frozenset: Immutable set
    "boolean": True,                    # bool: Boolean value
    "bytes": b'hello',                  # bytes: Immutable sequence of bytes
    "bytearray": bytearray([65, 66, 67]),  # bytearray: Mutable sequence of bytes
    "memoryview": memoryview(bytes(5)), # memoryview: View of memory buffers
    "none": None,                       # None: Absence of value
    "z":dict()
}

x, y, z = "Orange", "Banana", "Cherry"
ad,soyad,no="bahar","tercan",1234
fruits = ["apple", "banana", "cherry"] #Unpack a list:
x, y, z = fruits

""""
1. Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.
2. We should define function before we call it
"""

# print(sqrt(5))

#print("HELLO "*2) # HELLO HELLO 
#print([1, 2, 3]*2) # [1, 2, 3, 1, 2, 3]

############### CONDITON #############################################
#condition = if elif statement
x=8
if (0 < x) &(x < 10): 
    pass
else: 
   pass

if (0 < x < 10):
    pass
else: 
   pass

# liste içinde eleman arama
if (3 in [1,2,3,4,5]):
    pass
#Ternary Conditional: result = value_if_true if condition else value_if_false
result="OK" if 4>2 else "NO" #OK
############### CONDITON ##############################################


# #############  STRING ###############################################
s = "hello, world les!"
# Indexing
# print(s[0])  # Output: H (First character)
# print(s[-1])  # Output: ! (Last character)

# Slicing
# print(s[0:5])  # Output: Hello (Extracts characters from index 0 to 4)
# print(s[7:])   # Output: World! (Extracts from index 7 to the end)
# print(s[:5])   # Output: Hello (Extracts from the start to index 4)

# s[1]='r'#TypeError: 'str' object does not support item assignment

#Methods:
clean_text = s.strip() #Remove leading and trailing spaces
clean_text = s.strip() # Output: "Hello, World!"
upper_text = s.upper() # Output: " HELLO, WORLD! "
replaced_text = s.replace("World", "Python") # Output: " Hello, Python! "
index_of_comma = s.find(",") # Output: 5
words = s.split(",")  # Output: [' Hello', ' World! ']
sentence = " ".join(["Hello", "Python", "world!"]) # Output: "Hello Python world!"

# print(len(s))
# print(s[-3])
# print(s.capitalize().count("l"))
# print(s.title())
#  print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# #############  STRING ################################


########## RANGE ######################################
for i in range(1,10): #0'den 10'a kadar sayma
    pass

range(2,10,2)


for i in range(10,5,-1):
  pass
########## RANGE ######################################

########## LIST #######################################
# List Methods Cheatsheet
lst = [1, 2, 3]  # Initial list

lst.append(4)  # Adds 4 to the end of the list. Result: [1, 2, 3, 4]
lst.extend([5, 6])  # Adds multiple elements to the end. Result: [1, 2, 3, 4, 5, 6]
lst.insert(2, 99)  # Inserts 99 at index 2. Result: [1, 2, 99, 3, 4, 5, 6]
lst.remove(99)  # Removes (it doesn't return) first occurrence of 99. Result: [1, 2, 3, 4, 5, 6]
popped_item = lst.pop()  # Removes and returns last item. Result: [1, 2, 3, 4, 5], popped_item: 6
popped_item_at_index_2 = lst.pop(2)  # Removes and returns item at index 2. Result: [1, 2, 4, 5], popped_item_at_index_2: 3
lst.clear()  # Removes all items from the list. Result: []
lst = [1, 2, 3, 2]
index_of_2 = lst.index(2)  # Returns the index of the first occurrence of 2. Result: 1
count_of_2 = lst.count(2)  # Returns the number of occurrences of 2. Result: 2
lst.sort()  # Sorts the list in ascending order. Result: [1, 2, 2, 3]
lst.reverse()  # Reverses the list. Result: [3, 2, 2, 1]
lst_copy = lst.copy()  # Creates a shallow copy of the list. Result: [3, 2, 2, 1]
joined_words = ", ".join(["apple", "banana", "cherry"])  # Joins list elements into a string. Result: "apple, banana, cherry"
sliced_lst = lst[1:3]  # Slices the list from index 1 to 2. Result: [2, 2]
sliced_lst_start = lst[:2]  # Slices the list from the start to index 1. Result: [3, 2]
sliced_lst_end = lst[2:]  # Slices the list from index 2 to the end. Result: [2, 1]
sliced_lst_step = lst[::2]  # Slices the list every 2nd element. Result: [3, 2]
reversed_lst = lst[::-1]  # Reverses the list using slicing. Result: [1, 2, 2, 3]
lst_concatenated = lst + [7, 8]  # Concatenates two lists. Result: [3, 2, 2, 1, 7, 8]
lst_repeated = lst * 2  # Repeats the list. Result: [3, 2, 2, 1, 3, 2, 2, 1]
length_of_lst = len(lst)  # Returns the length of the list. Result: 4
lst.index(2)
# list[start:stop:step] #Slicing Syntax
# for index, value in enumerate(lst):

# ******string to array
list("bahar") #['b', 'a', 'h', 'a', 'r']
s='yorulmuş olmalısınız değil mi?'
s.split() #['yorulmuş', 'olmalısınız', 'değil', 'mi?']
s='çok-yorulduk-bitirelim' #['çok', 'yorulduk', 'bitirelim']
s.split('-')
ayirac=' '
t = ['deneme', 'dene', 'de', 'di']
ayirac.join(t)

#DELETING ELEMENT
# pop(index)
# - Removes element by **index**
# - Returns the removed element
# - Modifies the list
# - Raises IndexError if index is out of range

# remove(value)
# - Removes first occurrence of **value**
# - Does not return the removed element
# - Modifies the list
# - Raises ValueError if value is not found

# del index
# - Removes element by **index**
# - Does not return the removed element
# - Modifies the list
# - Raises IndexError if index is out of range

#****CONCATENATION
########## LIST #######################################

########## DICTIONARY ################################
z = {'bir': 'birinci', 'iki': 'ikinci', 'uc': 'ucuncu'}

len(z)  # Output: 3
z.get("ad")  # Output: None, z.get("iki")  # Output: 'ikinci'
'ders' in z  # Output: False, 'iki' in z  # Output: True
z.keys()  # Output: dict_keys(['bir', 'iki', 'uc'])
z.values()  # Output: dict_values(['birinci', 'ikinci', 'ucuncu'])
z.items()  # Output: dict_items([('bir', 'birinci'), ('iki', 'ikinci'), ('uc', 'ucuncu')])
z.pop('bir')  # Output: 'birinci', z  # Output: {'iki': 'ikinci', 'uc': 'ucuncu'}
z.popitem()  # Output: ('uc', 'ucuncu'), z  # Output: {'iki': 'ikinci'}
z.clear()  # Output: {}
z.update({'uc': 'ucuncu'})  # Output: {'uc': 'ucuncu'}
z.setdefault('dort', 'dorduncu')  # Output: 'dorduncu', z  # Output: {'uc': 'ucuncu', 'dort': 'dorduncu'}
dict.fromkeys(['a', 'b', 'c'], 0)  # Output: {'a': 0, 'b': 0, 'c': 0}

########## DICTIONARY ################################


########## TUPLE ################################
#tuples: virgülle ayrılmış değerler dizisi
t = 'a', 'b', 'c', 'd', 'e'
tuple1 = (1, 2, 3)
tuple2= (4,5,6)
tuple3= (1,3)

len(tuple1)  # Output: 3
2 in tuple1  # Output: True, 4 in tuple1  # Output: False

tuple1.index(2)  # Output: 1: Get the index of an element in the tuple (raises ValueError if not found)
tuple1.count(2)  # Output: 1
tuple2 = (4, 5, 6), tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)

# 7. repetition - Repeat a tuple using '*' operator
tuple3 = (1, 2), tuple3 * 3  # Output: (1, 2, 1, 2, 1, 2)

# 8. slicing - Access a portion of the tuple using slicing
tuple1[1:3]  # Output: (2, 3), tuple1[:2]  # Output: (1, 2), tuple1[::2]  # Output: (1, 3)

# 9. unpacking - Assign tuple elements to variables
a, b, c = tuple1  # Output: 1 2 3

# 10. max() - Get the maximum value from the tuple
max(tuple1)  # Output: 3

# 11. min() - Get the minimum value from the tuple
min(tuple1)  # Output: 1

# 12. sum() - Get the sum of all elements in the tuple
sum(tuple1)  # Output: 6

# 13. tuple() - Convert a list to a tuple
list1 = [1, 2, 3]
tuple(list1)  # Output: (1, 2, 3)

# 14. immutable nature of tuple - Cannot modify, add, or remove elements after creation
# tuple1[0] = 10  # TypeError: 'tuple' object does not support item assignment


# Using divmod
"""
In Python, the divmod() function takes two numbers and returns a tuple containing 
  their quotient and remainder when performing integer division.
  a is the dividend (the number you are dividing).
  b is the divisor (the number you are dividing by).
"""
quotient, remainder = divmod(10, 3)
# print(quotient)  # Output: 3
# print(remainder)  # Output: 1

# Without divmod
quotient = 10 // 3
remainder = 10 % 3
# print(quotient)  # Output: 3
# print(remainder)  # Output: 1

#***********
# ZIP : zip(iterable1, iterable2, ...)
#----------------Combining two lists------------------------------------------
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = zip(list1, list2)
# Convert the result into a list to view it
print(list(result))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
#----------------Different lengths:------------------------------------------
list1 = [1, 2, 3]
list2 = ['a', 'b']
result = zip(list1, list2)
# Convert the result into a list to view it
print(list(result))  # Output: [(1, 'a'), (2, 'b')]
#----------------Iterating over the zipped result:-----------------------------
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for x, y in zip(list1, list2):
    print(f"{x}: {y}")
#----------------Zipping more than two lists:-----------------------------
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

result = zip(list1, list2, list3)
print(list(result))  # Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
#----------------Unzipping using zip(*iterables)-----------------------------
zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped = zip(*zipped)
unzipped_list = list(unzipped)

print(unzipped_list)  # Output: [(1, 2, 3), ('a', 'b', 'c')]


#***********
########## TUPLE ################################




########## SORTING ###################################
t=['z', 'b', 'k' ,'a']
t.sort(reverse=True) # tersten sıralama 
# print(t)
########## SORTING ###################################

########## LOOP ###################################
# [expression for item in iterable if condition]
# Get squares of even numbers from 0 to 9
squares_of_even_numbers = [x**2 for x in range(10) if x % 2 == 0]
# print(squares_of_even_numbers)  # Output: [0, 4, 16, 36, 64]

demo= [(x+4) for x in [0,1,2,3,4,5] if (x+4) <7]
# print(demo) 
########## LOOP ###################################

##################Dosyalar#######################################
#dosyaya yazma
# fout=open("Desktop/yazmalik_dosya.txt", 'w') # burada w dosyayı yazmak üzere açtığımızı gösterir
# satir1="ilk satır\n"
# satir2="ikinci satır\n"
# fout.write(satir1)
# fout.write(satir2)
# fout.write(str(52)+"\n") #yazılacak öğenin string olması gerekli
# fout.write('%d aydır çalışıyorum, sınavdan %g %s.' %(3, 82.5, 'aldım'))
# fout.close()

cwd = os.getcwd()#pwd ile aynı çalışma klasörünü gösterir

os.path.exists('Desktop') #var mı? klasör örneği kullanıldı ancak dosya için de kullanılabilir
os.path.abspath("hakan") #mutlak yolu gösterir  klasör örneği kullanıldı ancak dosya için de kullanılabilir
os.path.isdir('Desktop/yazmalik_dosya.txt')#klasör  mü?
os.path.isfile('Desktop/yazmalik_dosya.txt')#dosya mı?
os.listdir(cwd)# bulunduğum klasörün içindeki dosya ve klasörler
#################Dosyalar#######################################

print (cwd)

# FUNCTION
def sum(x,y):
    return x + y

# print(sum(10,8))



########## FUNCTION ###################################
"""
Arbitrary Number of Arguments (*args and **kwargs)
*args: Allows a function to accept any number of positional arguments.
**kwargs: Allows a function to accept any number of keyword arguments.
"""
def print_numbers(*args):
    # print(args) #tuple
    for num in args:
        print(num)

# print_numbers(1, 2, 3, 4)  # Outputs 1, 2, 3, 4

def print_info(**kwargs):
    # print(kwargs["age"]) #dict
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# print_info(name="Alice", age=30)  # Outputs 'name: Alice' and 'age: 30'

add = lambda a, b: a + b #lambda arguments: expression
########## FUNCTION ###################################

print('%g' % 123.456)  # Output: 123.456 (normal decimal format)
print('%g' % 0.0001234)  # Output: 1.234e-04 (scientific notation)
print('%g' % 123456789.12345)  # Output: 1.23457e+08 (scientific notation)
