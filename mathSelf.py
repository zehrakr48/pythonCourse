number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


class Math:
    def add(self, number1, number2):
        return number1 + number2

    def subtract(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def divide(self, number1, number2):
        return number1 / number2


math = Math()
process = int(
    input(
        "\nSelect the operation you want to perform: \n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n"
    )
)

if process == 1:
    print("Result = " + str(math.add(number1, number2)))
elif process == 2:
    print("Result = " + str(math.subtract(number1, number2)))
elif process == 3:
    print("Result = " + str(math.multiply(number1, number2)))
elif process == 4:
    print("Result = " + str(math.divide(number1, number2)))
else:
    print("Invalid input!")
