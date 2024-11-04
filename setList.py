# Sets consist of unique, unordered elements without indexes.
# Duplicate values are not allowed; each element is unique.
# Sets provide efficient data storage.
# Elements in a set cannot be modified, but new elements can be added.

setList = {"Purple", "Blue", "Orange", "Pink", "Green"}
print(setList)

# Loop through each element in the set and print it
for color in setList:
    print(color)

# Check if 'Purple' is in the set (case-sensitive)
print("Is 'Purple' in the list?", "Purple" in setList)
print("Is 'purple' in the list?", "purple" in setList)

# Case-sensitive check with conditional statements
if "Purple" in setList:
    print("'Purple' is in the list.")
    if "purple" in setList:
        print("'purple' is in the list.")
else:
    print("'purple' is not in the list.")

# Add a single element to the set
setList.add("Black")
print(setList)

# Add multiple elements to the set at once
setList.update(["White", "Red", "Gray"])
print(setList)

# Remove an element if it exists, without an error if it doesn’t
setList.discard("Khaki")
print(setList)

# Delete the entire set
del setList
