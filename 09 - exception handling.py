# Basic try/catch block
try:
    result = 10 / 0 # Code that might raise an exception
except:
    print("An error occurred!") # Code to handle the exception

print("The program continues to run.")


# Handling Specific Exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"10 divided by {number} is {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
# The Else and Finally Clauses
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"10 divided by {number} is {result}")
finally:
    print("Thank you for using our division calculator!")
    
    
    
#Raising Exceptions
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as e:
    print(e)
    

# Custom Exceptions
class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    print(f"Age set to {age}")

try:
    set_age(-5)
except NegativeAgeError as e:
    print(e)