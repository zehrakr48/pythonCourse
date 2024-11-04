# Define two sets with color elements
colourList1 = {"Purple", "Blue", "Orange", "Pink", "Green", "Red", "Maroon"}
colourList2 = {"Black", "White", "Khaki", "Beige", "Brown", "Red", "Maroon"}

# Set union operation: combines two sets, removing duplicate elements
print("-------------set union-------------")
print(colourList1)
print(colourList2)
print(colourList1.union(colourList2))

# Set intersection operation: finds common elements between two sets
print("-------------set intersection-------------")
print(colourList1 & colourList2)
print(colourList1.intersection(colourList2))

# Set difference operation: finds elements in one set but not in the other
print("-------------set difference-------------")
print(colourList1 - colourList2)  # Elements in colourList1 but not in colourList2
print(colourList2 - colourList1)  # Elements in colourList2 but not in colourList1

# Set symmetric difference operation: finds elements unique to each set
print("-------------set symmetric difference-------------")
print(colourList1 ^ colourList2)
print(colourList1.symmetric_difference(colourList2))
