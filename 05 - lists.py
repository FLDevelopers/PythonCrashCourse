items = ["apple", "banana", "cherry","mangos","banana"]
mixed_list = [1, "hello", 3.14, True]

# Accessing items in a list
print(items)
print(items[0])
print(mixed_list[1])

# Negative indexing
print(items[-1])
print(items[-2])

# Slicing
print(items[1:3])

# append() 
items.append("berry")
print(items)

# insert() 
items.insert(1, "blueberry")
print(items)

# remove()
items.remove("banana")
print(items)

# pop()
last_fruit = items.pop()
print(last_fruit)
print(items)

# len() 
print(len(items))

# sort()
numbers = [9,1,5,9,3,8,7,4]
numbers.sort()
print(numbers)

# reverse()
items.reverse()
print(items)