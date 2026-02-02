"""
Python Fundamentals and OOP Practice
Author: Aaditya
Description: Practice code covering Python basics, data structures,
functions, and object-oriented programming.
"""

# ============================
# 1. BASIC PYTHON
# ============================

# Printing
print("Hello from Python!")

# Variables
name = "Aaditya"
age = 24
print(name, age)

# Type checking
print(type(name))
print(type(age))


# ============================
# 2. USER INPUT
# ============================

# Uncomment to test input
# color = input("What is your favourite color: ")
# print(f"Your favourite color is {color}")


# ============================
# 3. NUMBERS & BUILT-IN FUNCTIONS
# ============================

print(abs(-10))
print(round(3.6))

import math
print(math.ceil(4.2))
print(math.floor(4.9))


# ============================
# 4. STRINGS
# ============================

s = "hello"

# Indexing
print(s[0])
print(s[-1])

# Slicing
print(s[::-1])  # reverse string

# String methods
print(s.upper())
print(s.capitalize())


# ============================
# 5. LISTS
# ============================

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

from random import shuffle
shuffle(my_list)
print(my_list)


# ============================
# 6. TUPLES & SETS
# ============================

# Tuple
t = (1, 2, 3)
print(t[0])

# Set
unique_letters = set("Mississippi")
print(unique_letters)


# ============================
# 7. DICTIONARIES
# ============================

d = {
    "k1": [
        {"nest_key": ["this is deep", ["hello"]]}
    ]
}

print(d["k1"][0]["nest_key"][1][0])


# ============================
# 8. BOOLEAN LOGIC
# ============================

print(2 <= 3 >= 1)  # chained comparison


# ============================
# 9. LOOPS
# ============================

st = "Print only the words that start with s in this sentence"

for word in st.split():
    if word.lower().startswith("s"):
        print(word)


# ============================
# 10. FUNCTIONS
# ============================

def my_name(name):
    print(f"My name is {name}")

my_name("Aaditya")


def find_employee(work_hours):
    current_max = 0
    employee_of_month = ""

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return employee_of_month, current_max


work_hours = [("Charan", 50), ("Abhinav", 20), ("Aaditya", 60)]
print(find_employee(work_hours))


# ============================
# 11. *args and **kwargs
# ============================

def myfunc(*args):
    return [x for x in args if x % 2 == 0]

print(myfunc(1, 2, 3, 4, 5))


def myfunc_kwargs(**kwargs):
    if "fruit" in kwargs:
        print(f"My favourite fruit is {kwargs['fruit']}")

myfunc_kwargs(fruit="apple", veggie="carrot")