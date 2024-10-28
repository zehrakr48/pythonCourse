# Define the first string
string1 = "python is awesome!"

# Define the second string with different case
string2 = "PYTHON is AWESOME!"

# Define the third string with a different word
string3 = "PYTHON ist toll!"

# Compare string1 and string2 by converting both to uppercase
if string1.upper() == string2.upper():
    print("string1 and string2 are the same.")
else:
    print("string1 and string2 are not the same.")

# Compare string1 and string3 by converting both to uppercase
if string1.upper() == string3.upper():
    print("string1 and string3 are the same.")
else:
    print("string1 and string3 are not the same.")
