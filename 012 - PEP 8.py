# Indentation
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

     
# Maximum Line Length  
long_string = ("This is a very long string that we don't want to extend beyond "
               "79 characters, so we split it across multiple lines.")

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
    
    
# Imports
import os
import sys

from datetime import datetime
from math import pi, sqrt
# rest of the code down here


# Function and Variable Names
def calculate_area(length, width):
    return length * width

total_area = calculate_area(10, 20)


#Class Names
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
        
# Constants
MAX_SPEED = 120
PI = 3.14159


#Use Descriptive Names
# Not so good
def calc(a, b):
    return a * b

# Much better
def calculate_rectangle_area(length, width):
    return length * width


#Comments
# Bad: Multiplies length by width
area = length * width # type: ignore

# Good: Calculate area for irregular shapes
area = length * width * shape_factor # type: ignore


#String Formatting
name = "Alice"
age = 30
print(f"{name} is {age} years old")


#White Spaces
def complex_function():
    # Section 1: Data preparation
    data = load_data() # type: ignore
    cleaned_data = clean_data(data) # type: ignore
    
    # Section 2: Data processing
    result = process_data(cleaned_data) # type: ignore
    
    # Section 3: Result output
    save_result(result) # type: ignore
    print("Processing complete")
    

#List Comprehensions 
# Simple and readable
squares = [x**2 for x in range(10)]

# Too complex, better to use a for loop
matrix = [[i*j for j in range(5)] for i in range(5) if i % 2 == 0]
