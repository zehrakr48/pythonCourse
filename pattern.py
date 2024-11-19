number = int(input("Bir sayı girin: "))
star = ""  # Initialize an empty string to store the stars

for x in range(number):
    star += "*"  # Add a star to the string in each iteration
    print(star)
