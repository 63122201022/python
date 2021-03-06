# -*- coding: utf-8 -*-
"""022-Colab20210119-PyCharmReplica

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E010H_rnywZxRAGCts4BnaWnRtoP5U7p
"""

print("Hello, world! My name is kananek")

# This is the comment for the comments.py file
print("Hello!")  # this comment is for the second line

print("# this is not a comment")
# มีไว้สำหรับแสดลงข้อความ

a = b = 2  # This is called a "chained assignment". It assigns the value 2 to variables "a" and "b".
print("a = " + str(a))   # We'll explain the expression str(a) later in the course. For now it is used to convert the  variable "a" to a string.
print("b = " + str(b))

greetings = "greetings"
print("greetings = " + str(greetings))
greetings = 5
print("greetings = " + str(greetings))

variable = 1
print(variable)

## Variable types

number = 9
print(type(number))   # print type of variable "number"

float_number = 9.0
print(type(float_number))

number = 9
print(type(number))   # print type of variable "number"

float_number = 9.0
print(float_number)
print(int(float_number))

number = 9.0        # float number

result = number / 2

remainder = number % 2

print("result = " + str(result))
print("remainder = " + str(remainder))

number = 9.0        # float number

result = number / 2

remainder = number % 2

print("result = " + str(result))
print("remainder = " + str(remainder))

two = 2
three = 3

is_equal = two == three

print(is_equal)

one = 1
two = 2
three = 3

print(one < two < three)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.

is_greater = three > two
print(is_greater)

one = 1
two = 2
three = 3

print(one < two < three)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.

is_greater = three > two
print(is_greater)

hello = "hello"
ten_of_hellos = hello * 10
print(ten_of_hellos)

python = "Python"
print("h " + python[3])     # Note: string indexing starts with 0

p_letter = python[0]
print(p_letter)

long_string = "This is a very long string!"
exclamation = long_string[-1]
print(exclamation)

monty_python = "Monty Python"
monty = monty_python[:5]      # one or both index could be dropped. monty_python[:5] is equal to monty_python[0:5]
print(monty)
python = monty_python[6:]
print(python)

ice_cream = "ice cream"
print("cream" in ice_cream)    # print boolean result directly

contains = "ice" in ice_cream
print(contains)

phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:int(len(phrase)/2)]
print(first_half)

dont_worry = "Don't worry about apostrophes"
print(dont_worry)
print("\"Sweet\" is an ice-cream")
print('The name of this ice-cream is "Sweet\'n\'Tasty"')

monty_python = "Monty Python"
print(monty_python)

print(monty_python.lower())    # print lower-cased version of the string

print(monty_python.upper())

name = "John"
print("Hello, PyCharm! My name is %s!" % name)     # Note: %s is inside the string, % is after the string

print("I'm %d years old" % 27)

squares = [1, 4, 9, 16, 25]   # create new list
print(squares)

print(squares[1:4])

animals = ["elephant", "lion", "tiger", "giraffe"]  # create new list
print(animals)

animals += ["monkey", "dog"]    # add two items to the list
print(animals)

animals.append("dino")   # add one more item to the list using append() method
print(animals)

animals[-1] = "dinosaur"
print(animals)

animals = ["elephant", "lion", "tiger", "giraffe", "monkey", "dog"]  # create new list
print(animals)

animals[1:3] = ["cat"]    # replace 2 items -- "lion" and "tiger" with one item -- "cat"
print(animals)

animals[1:3] = []     # remove 2 items -- "cat" and "giraffe" from the list
print(animals)

animals[:] = []
print(animals)

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

print(len(alphabet))

# create new dictionary.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" are keys and numbers are values
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book
del phone_book ["John"]

print(phone_book ["Jane"])

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}  # create new dictionary
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 456
print(phone_book)

print(phone_book.keys())

print(phone_book.values())

grocery_list = ["fish", "tomato", "apples"]   # create new list

print("tomato" in grocery_list)    # check that grocery_list contains "tomato" item

grocery_dict = {"fish": 1, "tomato": 6, "apples": 3}   # create new dictionary

print("fish" in grocery_dict.keys())

name = "John"
age = 17

print(name == "John" or age == 17)    # checks that either name equals to "John" OR age equals to 17

print(name == 'John' and age != 23)

name = "John"
age = 17

print(name == "John" or not age > 17)

print(name == "John" or not age > 17)

print(name is "Ellis" or not (name is "John" and age == 17))

name = "John"
age = 17

if name == "John" or age == 17:   # check that name is "John" or age is 17. If so print next 2 lines.
    print("name is John")
    print("John is 17 years old")

tasks = ["task1", "task2"]    # create new list

if len(tasks) == 0:
    print("empty")

x = 28

if x < 0:
    print('x < 0')                      # executes only if x < 0
elif x == 0:
    print('x is zero')                 # if it's not true that x < 0, check if x == 0
elif x == 1:
    print('x == 1')                    # if it's not true that x < 0 and x != 0, check if x == 1
else:
    print('non of the above is true')

name = "John"
if name == "John":
    print(True)
else:
    print(False)

for i in range(5):    # for each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    print(i)          # this line is executed 5 times. First time i equals 0, then 1, ...


primes = [2, 3, 5, 7]   # create new list

for prime in primes:
    print(prime)

hello_world = "Hello, World!"

for ch in hello_world:    # print each character from hello_world
    print(ch)

length = 0      # initialize length variable

for ch in hello_world:
    length += 1     # add 1 to the length on each iteration

print(len(hello_world) == length)

square = 1

while square <= 10:
    print(square)    # This code is executed 10 times
    square += 1      # This code is executed 10 times

print("Finished")  # This code is executed once

square = 0
number = 1

while square < 81:
    square = number ** 2
    print(square)
    number += 1

count = 0

while True:  # this condition cannot possibly be false
    print(count)
    count += 1
    if count >= 5:
        break           # exit loop if count >= 5


zoo = ["lion", "tiger", "elephant"]
while True:                         # this condition cannot possibly be false
    animal = zoo.pop()       # extract one element from the list end
    print(animal)
    if animal == "elephant":
        break           # exit loop

for i in range(5):
    if i == 3:
        continue   # skip the rest of the code inside loop for current i value
    print(i)

for x in range(10):
    if x % 2 == 0:
        continue   # skip print(x) for this loop
    print(x)

def hello_world():  # function named my_function
    print("Hello, World!")

for i in range(5):
    hello_world()   # call function defined above 5 times

print('I want to be a function')
print('I want to be a function')
print('I want to be a function')


def fun():
    print('I want to be a function')

for i in range(3):
    fun()

def foo(x):                 # x is a function parameter
    print("x = " + str(x))

foo(5)   # pass 5 to foo(). Here 5 is an argument passed to function foo.

def square(x):
    print(x ** 2)

square(4)
square(8)
square(15)
square(23)
square(42)

def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = a + b
        a = tmp_var
    return result

print(fib(10))

def multiply_by(a, b=2):
    return a * b

print(multiply_by(3, 47))
print(multiply_by(3))    # call function using default value for b parameter


def hello(subject, name="John"):
    print("Hello %s! My name is %s" % (subject, name))

hello("PyCharm", "Jane")    # call "hello" function with "PyCharm as a subject parameter and "Jane" as a name
hello("PyCharm")            # call "hello" function with "PyCharm as a subject parameter and default value for the name

class MyClass:
    variable = 4

    def foo(self):   # we'll explain self parameter later in task 4
        print("Hello from function foo")

my_object = MyClass()  # variable "my_object" holds an object of the class "MyClass" that contains the variable and the "foo" function

class MyClass:
    variable1 = 1
    variable2 = 2

    def foo(self):     # we'll explain self parameter later in task 4
        print("Hello from function foo")

my_object = MyClass()
my_object1 = MyClass()

my_object.variable2 = 3     # change value stored in variable2 in my_object

print(my_object.variable2)
print(my_object1.variable2)

my_object.foo()   # call method foo() of object my_object

print(my_object.variable1)

class Car:
    color = ""
    def description(self):
        description_string = "This is a %s car." % self.color    # we'll explain self parameter later in task 4
        return description_string

car1 = Car()
car2 = Car()

car1.color = "blue"
car2.color = "red"

print(car1.description())
print(car2.description())

class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

class Square:

    def __init__(self):    # special method __init__
        self.sides = 4

square = Square()
print(square.sides)

class Car:
    def __init__(self, color):
        self.color = color

car = Car("blue")    # Note: you should not pass self parameter explicitly, only color parameter

print(car.color)

""" documentation string for module my_module
This module contains hello_world function
"""


def hello_world(name):
    print("Hello, World! My name is %s" % name)

import calculator

calc = calculator.Calculator()    # create new instance of Calculator class defined in calculator module
calc.add(2)
print(calc.get_current())

import my_module

my_module.hello_world("John")

"""
This module contains Calculator class
"""


class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

import datetime

print(datetime.datetime.today())

""" documentation string for module my_module
This module contains hello_world function
"""


def hello_world():
    return "Hello, World!"

"""
This module contains Calculator class
"""


class Calculator:
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def get_current(self):
        return self.current

from calculator import Calculator

calc = Calculator()    # here we can use Calculator class directly without prefix calculator.
calc.add(2)
print(calc.get_current())

from my_module import hello_world

print(hello_world())    # Note: hello_world function used without prefix

f = open("input.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                             # Note: if you want to write to the file use "w" as second argument

for line in f.readlines():   # read lines
    print(line)

f.close()                   # It's important to close the file to free up any system resources.

f1 = open("input1.txt", "r")

print(f1.readline())

f1.close()

zoo = ["lion", "elephant", "monkey"]

if __name__ == "__main__":
    f = open("output.txt", "a")

    for i in zoo:
        f.write(i)

    f.close()