number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))


class Math:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2


math = Math(number1, number2)
process = int(
    input(
        "\nSelect the operation you want to perform: \n1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n"
    )
)

if process == 1:
    print("Result = " + str(math.add()))
elif process == 2:
    print("Result = " + str(math.subtract()))
elif process == 3:
    print("Result = " + str(math.multiply()))
elif process == 4:
    print("Result = " + str(math.divide()))
else:
    print("Invalid input!")
