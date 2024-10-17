# Import The Entire Module
import math

print(math.pi)
print(math.sqrt(16))


# Import The Specific Items From The Modules
from math import pi, sqrt

print(pi)
print(sqrt(25))


# Import modules with an alias
import math as m

print(m.pi)


# Math Module
import math

print(math.pi)  # Pi constant
print(math.e)   # Euler's number
print(math.sqrt(25))  # Square root
print(math.sin(math.radians(30)))  # Sine of 30 degrees
print(math.log(100, 10))  # Log base 10 of 100


# Random Module
import random

print(random.random())  # Random float between 0 and 1
print(random.randint(1, 10))  # Random integer between 1 and 10
fruits = ['apple', 'banana', 'cherry']
print(random.choice(fruits))  # Random item from a list
random.shuffle(fruits)  # Shuffle a list in place
print(fruits)


# Date Time Module
from datetime import datetime, timedelta

now = datetime.now()
print(now)  # Current date and time
print(now.year)  # Current year
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formatted date and time

future = now + timedelta(days=7)
print(future)  # Date and time 7 days from now


# External Module
import requests # Run "pip install requests" command in termical to install requests module

response = requests.get("https://api.github.com")
print(response.status_code)  # HTTP status code
print(response.json())  # Response content as JSON