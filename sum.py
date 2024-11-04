# Get three numbers from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Add the numbers to a list
numbers = [number1, number2, number3]

sum = 0  # Initialize the total sum to zero
for number in numbers:  # Iterate through each number in the list
    sum += number  # Add each number to the total sum

# Print the result
print("The sum of the numbers is:", sum)  # Output the total sum
