#string
name = "John"
#integer
age = 30
#float
height = 5.9
#boolean
is_student = False
#list
fruits = ["apple", "banana", "cherry"]
#tuple
coordinates = (10.0, 20.0)

# Dictionary : key value pair , keys dont have to be same data type
person = {"name": "Alice", "age": 25}
x = {'key1': 4}
#print(x['key1'])  # Output: 4
x['key2'] = 5  # Adding a new key-value pair
#looping dictionary
for key, value in person.items():
    print(f"{key}: {value}")

for key in person:
    print(key)  

#set : no duplicates,  set are faster, order not maintained, uniqui  elements
unique_numbers = {1,2,3,4,5,6,7,8,9,10}
#x = set()   : this is an empty set
#print(unique_numbers)

#noneType
nothing = None
#print data types
""" print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(height))        # <class 'float'>
print(type(is_student))    # <class 'bool'>
print(type(fruits))        # <class 'list'>
print(type(coordinates))   # <class 'tuple'>
print(type(person))        # <class 'dict'>
print(type(unique_numbers)) # <class 'set'>
print(type(nothing))       # <class 'NoneType'>
 """

# BASIC OPERATIONS
# Arithmetic Operations
a = 10
b = 3 
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333...
print(a // b) # Floor Division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000

# String Operations
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!
repeated_greeting = greeting * 3
print(repeated_greeting)  # Output: HelloHelloHello

#list operations
numbers = [1, 2, 3]
print(len(numbers))  # Output: 3
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]
numbers.insert(1, 1.5) # Insert 1.5 at index 1
print(numbers)  # Output: [1, 1.5, 2, 3, 4]
numbers.pop() # Remove last element
print(numbers)  # Output: [1, 1.5, 2, 3]
numbers.extend([5, 6]) # Extend list with [5, 6]
print(numbers)  # Output: [1, 1.5, 2, 3, 5, 6]
numbers.remove(2) # Remove 2
print(numbers)  # Output: [1, 3, 4]
numbers.sort(reverse=True) # Sort in descending order
print(numbers)

# Dictionary Operations : key value pair 
person = {"name": "Alice", "age": 25}
person ["city"] = "New York" # Add new key-value pair
print(person) # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
del person["age"] # Remove key-value pair
print(person) # Output: {'name': 'Alice', 'city': 'New York'}

#set operations
unique_numbers = {1, 2, 3}
unique_numbers.add(4) # Add 4 to the set
print(unique_numbers) # Output: {1, 2, 3, 4}
unique_numbers.remove(2) # Remove 2 from the set
print(unique_numbers) #Output {1, 3, 4}

#tuple cannot be changed 
coordinates = (10.0, 20.0)
print(coordinates[0]) # Output: 10.0

#control structures
#if-else statement
num = 10
if num > 0:
    print("positive number")
elif num == 0:
    print("zero")
else:
    print("negative number")

#range
#start, stop, step
#range(1,10,2)

# For Loop
for i in range(5):
    print("iteration:", i)

for fruit in ["apple", "banana", "cherry"]:
    print("Fruit:", fruit)

for i, elem in enumerate[str](["a", "b", "c"]):
    print("index:", i, "element:", elem)

# While Loop
count = 0
while count < 5:
    print("count:", count)
    count += 1

#sliced
#sliced = [start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced = numbers[2:8:2]
print(sliced) # Output:  [2, 4, 6]
sliced_reverse = numbers[::-1]
print(sliced_reverse) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sliced_from_start = numbers[:5]
print(sliced_from_start) # Output: [0, 1, 2, 3, 4]
sliced_to_end = numbers[5:]
print(sliced_to_end) # Output: [5, 6, 7, 8, 9]

#functions definition
def greet(name):
    return "hello, " + name + "!"
print(greet("alice")) # Output: hello, alice!

def func(x, y):
    return x * y
print(func(4, 5)) # Output: 20

def func(x, y, z=None):
    return x * y, x/y

r1, r2 = func(10, 2)
print(r1) # Output: 20
print(r2) # Output: 5.0

def func(x):
    def func2():
        print(x)
    
    return func2

print(func(3)()) # Output: 3

x = [1,23,2454, 54]
print(x) # Output: [1, 23, 2454, 54]
print(*x) # Output: 1 23 2454 54    unpacking list

def func(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4), (5, 6)]

for pair in pairs:
    func(*pair) # Unpacking each tuple in the list

func(**{'x': 10, 'y': 20}) # Unpacking dictionary  # Output: 10 20


def func(*args, **kwargs):
    print(args, kwargs)

func(1, 2, 3, name="alice, age=30") # Output: (1, 2, 3) {'name': 'alice, age=30'}



# Class Definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"

person1 = Person("Bob", 28)
print(person1.introduce()) # Output: My name is Bob and I am 28 years old


# Importing Modules
import math
print("square root of 16 is :", math.sqrt(16))
import random
print("random number between 1 and 10 :", random.randint(1, 10))

# File Operations
with open("example.txt", "w") as file:
    file.write("holaaaaa!")

with open("example.txt", "r") as file:
    content = file.read()
    print("File content :", content)

# List Comprehensions
squares = [x**2 for x in range(10)]
print("Squares from 0 to 9 :", squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lambda Functions   = one line anonymous functions
add = lambda x, y: x + y
print("Sum using lambda :", add(5, 3)) # Output: 8

# Map and Filter
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

x = [2,3,8,12,76,23,53]
mp = map(lambda x: x*2, x) # Output: [4, 6, 16, 24, 152, 46, 106]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("even numbers", even_numbers)

#generators
def generate_numbers(n):
    for i in range(n):
        yield i
gen = generate_numbers(5) 
for number in gen:
    print("Generated number:", number)  # Output: 0, 1, 2, 3, 4

#decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed before", original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function
@decorator_function
def display():
    print("display function executed.")
display() # Output: wrapper executed before display
            #         display function executed.

















