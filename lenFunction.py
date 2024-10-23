loans = [
    "Fast Loan",
    "Special for those receiving their salary from this bank",
    "Retiree personal loan",
]

print(loans)  # Prints the entire list of loans
print(loans[0])  # Prints the first loan option: "Fast Loan"
print(
    loans[1]
)  # Prints the second loan option: "Special for those receiving their salary from this bank"
print(loans[2])  # Prints the third loan option: "Retiree personal loan"

print(len(loans))  # Prints the length of the list

loans[0] = "Quick Loan"  # Updates the first loan option to "Quick Loan"
print(loans)  # Prints the updated list of loans
