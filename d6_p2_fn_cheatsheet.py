
# ---------------------------------------------
# PYTHON FUNCTIONS - COMPLETE CHEAT SHEET
# ---------------------------------------------

# Basic Function Declaration and Calling
def fun():
    print("Welcome to GFG")

fun()  # Output: Welcome to GFG

# Function with Parameters and Return Type
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    return num1 + num2

print(f"The addition of 5 and 15 results {add(5, 15)}.")

# Function with Logic - Prime Checker
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

print(is_prime(78), is_prime(79))  # Output: False True

# Function Arguments Types
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)

# Default Arguments
def myFun(x, y=50):
    print("x:", x)
    print("y:", y)

myFun(10)

# Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)

student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')

# Positional Arguments
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj")

# Arbitrary Non-Keyword Arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Arbitrary Keyword Arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

myFun(first='Geeks', mid='for', last='Geeks')

# Docstring Example
def evenOdd(x):
    """Function to check if the number is even or odd"""
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

print(evenOdd.__doc__)

# Nested Functions
def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
    f2()

f1()

# Anonymous Function (lambda)
def cube(x): return x*x*x
cube_v2 = lambda x: x*x*x

print(cube(7))
print(cube_v2(7))

# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

# Return Statement
def square_value(num):
    return num**2

print(square_value(2))
print(square_value(-4))

# Pass by Reference
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# Breaking Reference
def myFun(x):
    x = [20, 30, 40]

lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)

# Breaking Reference for Immutable
def myFun(x):
    x = 20

x = 10
myFun(x)
print(x)

# Swap Function Demo
def swap(x, y):
    temp = x
    x = y
    y = temp

x = 2
y = 3
swap(x, y)
print(x)
print(y)

# ---------------------------------------------
# NICE-TO-HAVE EXTRAS
# ---------------------------------------------

# Function Annotations
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(3, 4))

# Keyword-Only Arguments
def describe_pet(*, name: str, animal: str = "dog"):
    print(f"I have a {animal} named {name}.")

describe_pet(name="Buddy")
describe_pet(name="Milo", animal="cat")

# Variable Scope
global_var = "I am global"
def scope_demo():
    local_var = "I am local"
    print(global_var)
    print(local_var)
scope_demo()

# global keyword
count = 0
def increment():
    global count
    count += 1
increment()
print(f"Global count is: {count}")

# Function Aliasing
def say_hi():
    print("Hi there!")

greeting = say_hi
greeting()

# Higher-Order Functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(style, message):
    return style(message)

print(speak(shout, "Hello World!"))
print(speak(whisper, "Hello World!"))

# Using map and filter
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Decorators
def simple_decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
