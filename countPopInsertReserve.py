cars = list(
    (
        "Volvo",
        "Mercedes",
        "Skoda",
        "Toyota",
        "Mercedes",
        "Volvo",
        "Nissan",
        "Fiat",
        "Renault",
        "Dacia",
        "Skoda",
        "Volvo",
        "Hyundai",
        "Nissan",
        "Fiat",
        "Peugeot",
    )
)

# Print the number of elements in the list
print("Number of elements in the list: " + str(len(cars)))

# Print the count of 'Volvo' in the list
print("Number of 'Volvo' in the list: " + str(cars.count("Volvo")))

# Print the index of the first occurrence of 'Peugeot' in the list
print("Index of 'Peugeot' in the list: " + str(cars.index("Peugeot")))

# Remove the 8th element from the list
cars.pop(7)

# Insert 'Peugeot' as the 8th element in the list
cars.insert(7, "Peugeot")

# Print the list after insertion
print(cars)

# Reverse the list
cars.reverse()

# Print the reversed list
print(cars)

# Clear the list and print it (clears all elements)
print("List after clearing all elements: " + str(cars.clear()))
