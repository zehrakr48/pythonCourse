# The only difference between a tuple and a normal list is that
# the elements of a tuple cannot be changed. A tuple is read-only.
tupleList = (1, 2, 3, 4, 5, 6, 7)
normalList = [1, 2, 3, 4, 5, 6, 7]

# tupleList[0] = 7  # This line would raise a TypeError because tuples are immutable
normalList[0] = 7  # Lists, however, can have their elements changed

# Print the second-to-last element in the tuple
print(tupleList[-2])

# Print the second-to-last element in the list
print(normalList[-2])

# Print only the element at index 1 from the tuple
print(tupleList[1:2])

# Print only the element at index 1 from the list
print(normalList[1:2])

# Define a tuple with a single element "Zehra"
tupleValue = ("Zehra",)

# Print the tuple to the console
print(tupleValue)
