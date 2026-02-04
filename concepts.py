"""
Python Practice – Generators, Decorators, Lambda
Covered:
- What generators are
- yield vs return
- Generator expressions
- How for-loops use iterators internally
- Common generator mistakes
- Decorators (without immediate execution)
- Lambda functions
- defaultdict with lambda
"""

# ---------------------------------
# GENERATORS: yield vs return
# ---------------------------------

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


# ---------------------------------
# GENERATOR PRESERVES STATE
# ---------------------------------

def count_numbers(n):
    for i in range(n):
        yield i

counter = count_numbers(5)

print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2


# ---------------------------------
# FOR LOOP USES ITERATORS INTERNALLY
# ---------------------------------

nums = [1, 2, 3]

iterator = iter(nums)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ---------------------------------
# GENERATOR EXPRESSION
# ---------------------------------

gen_expr = (x * x for x in range(4))

for value in gen_expr:
    print(value)


# ---------------------------------
# WHY THIS IS A GENERATOR
# (No yield keyword needed)
# ---------------------------------

nums = (x for x in range(3))
print(type(nums))  # <class 'generator'>


# ---------------------------------
# COMMON GENERATOR MISTAKE (FIXED)
# ---------------------------------

import random

def rand_num(low, high, n):
    for _ in range(n):
        yield random.randint(low, high)

for number in rand_num(1, 10, 5):
    print(number)


# ---------------------------------
# GENERATOR VS LIST (MEMORY IDEA)
# ---------------------------------

# List stores everything in memory
list_nums = [x for x in range(5)]

# Generator produces values one by one
gen_nums = (x for x in range(5))


# ---------------------------------
# DECORATORS: WITHOUT IMMEDIATE CALL
# ---------------------------------

def new_decorator(original_func):
    def wrap():
        print("Before function execution")
        original_func()
        print("After function execution")
    return wrap   # returning function, NOT calling it

@new_decorator
def function_need():
    print("I need a decorator")

function_need()


# ---------------------------------
# DECORATOR FLOW EXPLANATION
# ---------------------------------
# function_need = new_decorator(function_need)
# function_need()


# ---------------------------------
# LAMBDA FUNCTIONS
# ---------------------------------

# Normal function
def add(a, b):
    return a + b

# Lambda version
add_lambda = lambda a, b: a + b

print(add_lambda(5, 6))


# ---------------------------------
# LAMBDA WITH SORT
# ---------------------------------

names = [("Aaditya", 22), ("Charan", 20), ("Abhinav", 25)]

names_sorted = sorted(names, key=lambda x: x[1])
print(names_sorted)


# ---------------------------------
# DEFAULTDICT WITH LAMBDA
# ---------------------------------

from collections import defaultdict

scores = defaultdict(lambda: 0)

scores["math"] += 10
scores["science"] += 5

print(scores)


# ---------------------------------
# KEY TAKEAWAYS 
# ---------------------------------
# - Generators pause execution and resume with yield
# - They are memory efficient
# - for-loops work with iterators/generators internally
# - Decorators return functions, they do NOT execute immediately
# - Lambda functions are single-expression anonymous functions
