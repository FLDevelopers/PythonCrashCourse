#Get User Input
name = input("What's your name? ")
print("Hello, " + name + "!")

# Convert User Input
age = input("How old are you? ")
print(type(age))
new_age = int(age)
print(type(new_age))
print(f"Your age is {new_age}")

# Basic printing
print("Hello, World!")

# Printing multiple items
x = 5
y = 10
print(f"x = {x} and y = {y}")

# Printing with different separators
print("a", "b", "c", sep="-")
print("a", "b", "c", sep="*")
print("a", "b", "c", sep="/")

# Printing with a different end character
print("Hello")
print("World")

print("Hello", end=" ")
print("World")

#String Formatting
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

x = 10
y = 20
print(f"{x} + {y} = {x + y}")