# Get the current light color from the user
currentLight = input("Please enter the color of the current light: ").lower()

# Check the state of the light using match-case
match currentLight:
    case "red":
        print("Stop!")
    case "yellow":
        print("Ready!")
    case "green":
        print("Go!")
    case _:
        print("Invalid light color entered.")
