def factorial(number):
    if number < 0:
        raise ValueError("Factorial cannot be calculated for negative numbers!")
    elif number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial


# Get a number from the user and calculate its factorial
number = int(input("Enter a number: "))
try:
    result = factorial(number)
    print(number, "factorial is:", result)
except ValueError as e:
    print(e)
