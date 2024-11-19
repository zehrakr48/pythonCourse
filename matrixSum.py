def createMatrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter the element at row {i+1}, column {j+1}: "))
            row.append(element)
        matrix.append(row)

    return matrix


def addMatrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions.")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# Get user input for two matrices
matrix1 = createMatrix()
matrix2 = createMatrix()

# Add the matrices
sumMatrix = addMatrices(matrix1, matrix2)

# Print the result
print("Sum of the matrices:")
for row in sumMatrix:
    print(row)
