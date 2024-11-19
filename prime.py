number = int(input("Enter a number: "))

# Loop from 2 to one less than the number
for i in range(2, number):
    # If the number is divisible by any number in the range, it's not prime
    if number % i == 0:
        print("This number is not prime.")
        break

    # If the loop completes without breaking (i.e., no divisors found), the number is prime
    else:
        print("This number is prime.")
        break
