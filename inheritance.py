# init definition = constructor
class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age


person1 = Person("Zehra", "Kır", 22)
print("Person1 firstname:", person1.firstName)
print("Person1 lastName:", person1.lastName)
print("Person1 age:", person1.age)


# Thanks to these operations, the Worker class inherits from the Person class.
class Worker(Person):
    def __init__(self, firstName, lastName, age, salary):
        super().__init__(firstName, lastName, age)
        self.salary = salary


# Thanks to these operations, the Customer class inherits from the Person class.
class Customer(Person):
    def __init__(self, firstName, lastName, age, creditCardNumber):
        super().__init__(firstName, lastName, age)
        self.creditCardNumber = creditCardNumber


worker1 = Worker("Ahmet", "Kır", 33, 30000)
print("\nWorker1 firstname:", worker1.firstName)
print("Worker1 lastName:", worker1.lastName)
print("Worker1 age:", worker1.age)
print("Worker1 salary:", worker1.salary)

customer1 = Customer("Fatma", "Alkurt", 36, 123456789)
print("\nCustomer1 firstname:", customer1.firstName)
print("Customer1 lastName:", customer1.lastName)
print("Customer1 age:", customer1.age)
print("Customer1 creditCardNumber:", customer1.creditCardNumber)
