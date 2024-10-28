# Define a string containing personal information
bio1 = "Zehra KIR 22 Gaziantep"

# Split the string by whitespace and print the result
print(bio1.split())

# Define a string with components separated by periods
bio2 = "Zehra.KIR.22.Gaziantep"

# Split the string using '.' as a separator and print the result
print(bio2.split("."))

# Define a string with leading and trailing whitespace, separated by semicolons
bio3 = "    Zehra;KIR;22;Gaziantep    "

# Split the string using ';' as a separator and print the result
print(bio3.split(";"))

# Define the same string but strip leading and trailing whitespace
bio4 = "  Zehra;KIR;22;Gaziantep  ".strip()

# Split the cleaned string using ';' as a separator and print the result
print(bio4.split(";"))

# Print the city of residence, which is the last element after splitting
print("City of residence: " + bio4.split(";")[3])  # Extracts the city name directly
