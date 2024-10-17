# if/elif/else Statements
temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's a nice day.")
else:
    print("It's a bit chilly.")
    
    
# For Loops
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")
    
for i in range(5):
    print(f"For Loop Count: {i}")
    
    
# While Loops
count = 0

while count < 5:
    print(f"While Loop Count is {count}")
    count += 1
 
 
# Break And Continue Statements
for i in range(10):
    if i == 5:
        print("We've reached 5, stopping here.")
        break
    print(f"Break statement {i}")
    
for i in range(5):
    if i == 2:
        print("Skipping 2")
        continue
    print(f"Continue statement {i}")
  

#Match Statement
def grade_comment(grade): #Method with grade parameter
    match grade:
        case 'A':
            return "Excellent!"
        case 'B':
            return "Good job!"
        case 'C':
            return "You passed."
        case 'D' | 'F':
            return "You need to study more."
        case _:
            return "Invalid grade"

print(grade_comment('B')) 
print(grade_comment('F'))