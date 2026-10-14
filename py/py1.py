print("Hello, \nVS Code on Mac!")
#DATA TYPES
# String
name = "John Doe"
# Integer
age = 30
# Float
height = 5.9
# Boolean
is_student = False
# List
fruits = ["apple", "banana", "cherry"]
# Tuple
coordinates = (10.0, 20.0)



# Dictionary : key value pair , keys dont have to be same data type
person = {"name": "Alice", "age": 25}
x = {'key1': 4}  
print(x['key1'])  # Output: 4
x['key2'] = 5  # Adding a new key-value pair
#looping dictionary
for key, value in person.items():
    print(f"{key}: {value}")

for key in person:
    print(key)  



# Set : no duplicates,  set are faster, order not maintained, uniqui  elements
unique_numbers = {1, 2, 3, 4, 5}
#x = set()   : this is an empty set



# NoneType
nothing = None
# Print data types
print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(height))        # <class 'float'>
print(type(is_student))    # <class 'bool'>
print(type(fruits))        # <class 'list'>
print(type(coordinates))   # <class 'tuple'>
print(type(person))        # <class 'dict'>
print(type(unique_numbers)) # <class 'set'>
print(type(nothing))       # <class 'NoneType'>


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
print(name.upper())  # Output: ALICE
print(full_greeting)  # Output: Hello, Alice!
repeated_greeting = greeting * 3
print(repeated_greeting)  # Output: HelloHelloHello



# List Operations
numbers = [1, 2, 3]
print(len(numbers))  # Output: 3
numbers.append(4)  # Add 4 to the end
print(numbers)  # Output: [1, 2, 3, 4]
numbers.insert(1, 1.5)  # Insert 1.5 at index 1
print(numbers)  # Output: [1, 1.5, 2, 3, 4]
numbers.pop()  # Remove last element
print(numbers)  # Output: [1, 1.5, 2, 3]
numbers.extend([5, 6])  # Extend list with [5, 6]
print(numbers)  # Output: [1, 1.5, 2, 3, 5, 6]
numbers.remove(2)  # Remove 2
print(numbers)  # Output: [1, 3, 4]
numbers.sort(reverse=True)  # Sort in descending order
print(numbers)  # Output: [4, 3, 1]

# Dictionary Operations
person = {"name": "Bob", "age": 28}
person["city"] = "New York"  # Add new key-value pair
print(person)  # Output: {'name': 'Bob', 'age': 28, 'city': 'New York'}
del person["age"]  # Remove key-value pair
print(person)  # Output: {'name': 'Bob', 'city': 'New York'}

# Set Operations
unique_numbers = {1, 2, 3}
unique_numbers.add(4)  # Add 4 to the set
print(unique_numbers)  # Output: {1, 2, 3, 4}
unique_numbers.remove(2)  # Remove 2 from the set
print(unique_numbers)  # Output: {1, 3, 4}

#Tuple cannot be changed
coordinates = (10.0, 20.0) 
print(coordinates[0])  # Output: 10.0





# Boolean Operations
x = True
y = False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not x)    # Output: False
# NoneType Operations 
z = None
print(z is None)  # Output: True
print(z is not None)  # Output: False
# Type Conversion
num_str = "123"
num_int = int(num_str)  # Convert string to integer 
print(num_int)  # Output: 123
num_float = float(num_str)  # Convert string to float
print(num_float)  # Output: 123.0
str_from_int = str(num_int)  # Convert integer to string
print(str_from_int)  # Output: "123"
# Input and Output
#user_input = input("Enter something: ")
#print("You entered:", user_input)
# Comments
# This is a single-line comment

 

# Control Structures
# If-Else Statement
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#range
#start, stop, step
#range(1,10,2)
#if only one argument is given, it is considered as stop and start is 0

# For Loop
for i in range(5):
    print("Iteration:", i)

for fruit in ["apple", "banana", "cherry"]:
    print("Fruit:", fruit)

for i, elem in enumerate(["a", "b", "c"]):
    print("Index:", i, "Element:", elem)    



# While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1


#sliced
#sliced = [start:stop:step]
# Sliced Example
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced = numbers[2:8:2]
print("Sliced List:", sliced)  # Output: Sliced List: [2, 4, 6]
sliced_reverse = numbers[::-1]
print("Reversed List:", sliced_reverse)  # Output: Reversed List: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
sliced_from_start = numbers[:5]
print("First 5 elements:", sliced_from_start)  # Output: First 5 elements: [0, 1, 2, 3, 4]
sliced_to_end = numbers[5:]
print("Elements from index 5 to end:", sliced_to_end)  # Output: Elements from index 5 to end: [5, 6, 7, 8, 9]
 

# Function Definition
def greet(name):
    return "Hello, " + name + "!"
print(greet("Alice"))  # Output: Hello, Alice!

def func(x, y):
    return x * y
print(func(4, 5))  # Output: 20

def func(x, y, z=None):
    return x * y, x/y 

r1, r2 = func(10, 2)
print(r1)  # Output: 20
print(r2)  # Output: 5.0


def func(x):
    def func2():
        print(x)

    return func2

print(func(3)())


x = [1,23,2454, 54]
print(*x)  # Output: 1 23 2454 54    unpacking list


def func(x, y):
    print(x, y)

pairs = [(1, 2), (3, 4), (5, 6)]

for pair in pairs:
    func(*pair)  # Unpacking each tuple in the list

func(**{'x': 10, 'y': 20})  # Unpacking dictionary 

def func(*args, **kwargs):
    print(args, kwargs)

func(1, 2, 3, name="Alice", age=30)  # Output: (1, 2, 3) {'name': 'Alice', 'age': 30}





# Class Definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
person1 = Person("Bob", 28)
print(person1.introduce())  # Output: My name is Bob and I am 28 years old.



# Importing Modules
import math
print("Square root of 16 is:", math.sqrt(16))  # Output: 4.0
import random
print("Random number between 1 and 10:", random.randint(1, 10))
# File Operations
with open("example.txt", "w") as file:
    file.write("Hello, World!")
with open("example.txt", "r") as file:  
    content = file.read()
    print("File content:", content)  # Output: Hello, World!
# List Comprehensions
squares = [x**2 for x in range(10)]
print("Squares from 0 to 9:", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Lambda Functions   = one line anonymous functions
add = lambda x, y: x + y
print("Sum using lambda:", add(5, 3))  # Output: 8  



# Map and Filter
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

x = [2,3,8,12,76,23,53]
mp = map(lambda x: x*2, x) # Output: [4, 6, 16, 24, 152, 46, 106]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4]




# Generators
def generate_numbers(n):
    for i in range(n):
        yield i
gen = generate_numbers(5)
for number in gen:
    print("Generated number:", number)  # Output: 0, 1, 2, 3, 4
# Decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before", original_function.__name__)
        return original_function(*args, **kwargs)
    return wrapper_function
@decorator_function
def display():
    print("Display function executed.")
display()  # Output: Wrapper executed before display
            #         Display function executed.
# Modules and Packages
# Create a module named my_module.py with a function
# def my_function():
#     return "Hello from my_module!"
# Then import and use it
#import my_module
#print(my_module.my_function())  # Output: Hello from my_module!
# Virtual Environments
# Create a virtual environment using the command:
# python -m venv myenv
# Activate the virtual environment:
# On Windows: myenv\Scripts\activate
# On Mac/Linux: source myenv/bin/activate
# Deactivate the virtual environment using the command:
# deactivate
# Advanced Data Structures
from collections import namedtuple, deque, defaultdict, Counter
# Named Tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("Point:", p)  # Output: Point: Point(x=10, y=20)
# Deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", dq)  # Output: Deque: deque([0, 1, 2, 3, 4])
# DefaultDict
dd = defaultdict(int)   
dd['a'] += 1
dd['b'] += 2
print("DefaultDict:", dd)  # Output: DefaultDict: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# Counter
cnt = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print("Counter:", cnt)  # Output: Counter: Counter({'apple': 3, 'banana': 2, 'orange': 1})
# Date and Time
from datetime import datetime, timedelta
now = datetime.now()
print("Current Date and Time:", now)  # Output: Current Date and Time: 2024-06-XX XX:XX:XX.XXXXXX
future_date = now + timedelta(days=10)
print("Date after 10 days:", future_date)  # Output: Date after 10 days: 2024-06-XX XX:XX:XX.XXXXXX
# Regular Expressions
import re
pattern = r'\bfoo\b'
text = "foo bar baz foo"
matches = re.findall(pattern, text)
print("Matches found:", matches)  # Output: Matches found: ['foo', 'foo']
# Networking
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Hostname:", hostname)  # Output: Hostname: your_hostname
print("IP Address:", ip_address)  # Output: IP Address: your_ip_address
# Multithreading
import threading
def print_numbers():
    for i in range(5):
        print("Number:", i)
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
# Output: Number: 0
#         Number: 1
#         Number: 2
#         Number: 3
#         Number: 4
# Multiprocessing
import multiprocessing
def square(n):
    return n * n
if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print("Squared numbers using multiprocessing:", results)  # Output: Squared numbers using multiprocessing: [1, 4, 9, 16, 25]
# Web Scraping
import requests
from bs4 import BeautifulSoup
url = 'https://www.example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print("Page Title:", soup.title.string)  # Output: Page Title: Example Domain

