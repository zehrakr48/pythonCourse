file = open("lorem.txt")

# Reading and printing each line of the file
for line in file:
    print(line)

# %%
# file = open("customer.txt", "r")  # Read mode
# file = open("customer.txt", "w")  # Write mode
# file = open("customer.txt", "a")  # Append mode
# file = open("customer.txt", "x")  # Create mode (fails if file exists)

# Reading the entire file content
print(file.read())

# Reading the first line of the file
print(file.readline())
