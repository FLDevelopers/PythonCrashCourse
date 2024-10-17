#Defining Functions
def greet():
    print("Hello, World!")
    
greet()
greet()
greet()


# Parameters And Arguments
def greet(person_name):
    print(f"Hello, {person_name}!")
    
greet("Alice")


#Multiple Parameters
def describe_yourself(person_name, programming_language):
    print(f"I'm {person_name} and i'm learning {programming_language}.")

describe_yourself("John", "Python") 


#Default Values
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("John")
greet("Alice", greeting="Hi")


#Return Values
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

# We can use the returned value directly in other operations:
print(add(3, 5) * 2)


#Built-in Functions
print("I'm Printing")

print(len("Hello"))
print(len([1, 2, 3, 4]))

print(type(42))  
print(type("Hello"))

x = int("42")
y = float(x)
z = str(y)
print(x, y, z)

name = input("What's your name? ")
print(f"Nice to meet you, {name}!")