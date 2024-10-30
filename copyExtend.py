# Create a list named cars1 with car brands
cars1 = list(("Volvo", "Mercedes", "Skoda", "Nissan", "Bmw"))

# Assign cars1 to cars2 (both will point to the same list)
cars2 = cars1

# Create a copy of cars1 and assign it to cars3 (a new independent list)
cars3 = cars1.copy()

# Modify the fourth element of cars2 to "Audi"
cars2[3] = "Audi"

# Print the contents of cars1
print("Cars1 list: ", cars1)

# Print the contents of cars2 (same as cars1 due to the reference)
print("Cars2 list: ", cars2)

# Print the contents of cars3 (independent copy of the original cars1)
print("Cars3 list: ", cars3)

# Extend cars1 by appending all elements of cars3 to the end of cars1
cars1.extend(cars3)

# Print the combined list of cars1 and cars3
print("Cars1 list combined with Cars3 list: ", cars1)
