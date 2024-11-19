# Get the user's name as input
name = input("Enter your name: ")


# Define a function called say_hello
def say_hello(name="Visitor"):
    """
    This function greets the user with their name.
    If no name is provided, it greets the user as "Visitor".
    """
    print(f"Hello, {name}!")


# Check if the user entered a name
if name:
    # If a name was entered, call the function with the user's name
    say_hello(name)
else:
    # If no name was entered, call the function with the default name "Visitor"
    say_hello()
