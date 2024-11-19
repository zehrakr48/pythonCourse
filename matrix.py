def createMatrix():

    # Get the number of rows and columns from the user
    rows = int(input("Enter the number of rows for the matrix: "))
    columns = int(input("Enter the number of columns for the matrix: "))

    # Create an empty matrix
    matrix = []

    # Get matrix elements from the user
    for i in range(rows):
        row_elements = []
        for j in range(columns):
            element = int(
                input(f"Enter the element at row {i+1}, column {j+1} of the matrix: ")
            )
            row_elements.append(element)
        matrix.append(row_elements)

    # Print the created matrix
    print("\nCreated Matrix:")
    for row in matrix:
        print(row)


# Call the function to create a matrix
createMatrix()
