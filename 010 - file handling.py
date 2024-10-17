# Basic File Handling Code
file = open('example.txt', 'r')
file.close()

# File Handling using With statement
with open('example.txt', 'r') as file:
    # File operations here
    pass

# Read File Content using Read method
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
# Read File Content using Read Line method
with open('example.txt', 'r') as file:
    line = file.readline()
    print(line)
  
# Read File Content using Read Lines method  
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        
        
# Read File Content from File Object
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
        
# Write File       
with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
 
# Write Multiple Lines   
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)

# Appending Files   
with open('output.txt', 'a') as file:
    file.write("This line is appended to the end of the file.\n")