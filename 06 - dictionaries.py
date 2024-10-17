person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])

# Using the get() method
print(person.get("age"))
print(person.get("job", "Not specified"))

# keys() - returns a view of all keys
print(person.keys())

# items() - returns a view of all key-value pairs
print(person.items())

# update() - updates the dictionary with elements
person.update({"job": "Engineer", "age": 31})
print(person)

# pop() - removes the item with the specified key and returns its value
removed_age = person.pop("age")
print(removed_age) 
print(person)

# clear() - removes all items from the dictionary
person.clear()
print(person)

# lists in dictionary as values
student_grades = {
    "Alice": [85, 90, 92],
    "Bob": [78, 85, 80],
    "Charlie": [92, 88, 95]
}

print(student_grades["Bob"])
print(student_grades["Bob"][0])