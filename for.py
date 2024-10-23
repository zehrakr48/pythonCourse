students = ["fatma", "ahmet", "zehra", "ali", "ayfer", "enes", "bugra", "elisa"]

# Loop through each student. Each element of the iterated list is called an "alias".
print("students: ")
for student in students:
    print(student)

print("\n")

# Loop through numbers from 0 to 7 (8 is not included).
for i in range(8):
    print(i, " ")

print("\n")

# Loop through the length of the students list and print index + 1.
for i in range(len(students)):
    print(i + 1, " ")

print("\n")

# Loop through the list using the length of the students list to access each student.
print("students: ")
for i in range(len(students)):
    print(students[i], " ")

print("\n")

# Loop from index 3 to 4 (5 is not included) and print those elements from the list.
for i in range(3, 5):
    print(students[i], " ")

print("\n")

# Loop from index 0 to 12 (14 is not included) in steps of 2.
for i in range(0, 14, 2):
    print(i, " ")
