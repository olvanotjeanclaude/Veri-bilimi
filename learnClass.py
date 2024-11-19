# ----------------------------------------
# Basics of Classes
# ----------------------------------------
class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def greet(self):  # Instance method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example Usage
person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.

# ----------------------------------------
# Class Variables vs. Instance Variables
# ----------------------------------------
class Counter:
    count = 0  # Class variable (shared across instances)

    def __init__(self, name):
        self.name = name  # Instance variable (unique to each instance)
        Counter.count += 1  # Increment the class variable

# Example Usage
a = Counter("A")
b = Counter("B")
print(Counter.count)  # Output: 2 (shared across all instances)

# ----------------------------------------
# Static Methods and Class Methods
# ----------------------------------------
class Utility:
    counter = 0

    def __init__(self):
        Utility.counter += 1

    @classmethod
    def get_counter(cls):  # Class method
        return cls.counter

    @staticmethod
    def greet():  # Static method
        return "Hello, I'm a static method!"

# Example Usage
print(Utility.get_counter())  # Output: 0 (before creating instances)
u = Utility()
print(Utility.get_counter())  # Output: 1
print(Utility.greet())  # Output: Hello, I'm a static method!

# ----------------------------------------
# Inheritance
# ----------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Inherit from Animal class
    def speak(self):
        print(f"{self.name} barks")

# Example Usage
dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks

# ----------------------------------------
# Encapsulation: Public, Protected, and Private Members
# ----------------------------------------
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

# Example Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Private Attributes and Methods
class SecureAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def __private_method(self):  # Private method
        return "This is a private method"

    def access_private_method(self):  # Public method to access the private one
        return self.__private_method()

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

# Example Usage
secure_account = SecureAccount(1000)
secure_account.deposit(500)
print(secure_account.get_balance())  # Output: 1500

# Access private methods through a public method
print(secure_account.access_private_method())  # Output: This is a private method

# ----------------------------------------
# Encapsulation Example: Private Counters
# ----------------------------------------
class Sayıcı:
    __gizli_sayi = 0  # Private variable (cannot be accessed directly)

    def artir(self):
        self.__gizli_sayi += 1
        print(self.__gizli_sayi)

# Example Usage
sayac = Sayıcı()
sayac.artir()  # Output: 1
sayac.artir()  # Output: 2
