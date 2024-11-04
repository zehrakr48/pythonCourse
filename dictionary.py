# The dictionary function works like a dictionary (key-value pairs).
# Values can be modified, and new elements can be added.

print("-------------worterbuch-------------")
worterbuch = {"Katze": "Cat", "Hund": "Dog", "Schildkröte": "Turtle", "Fish": "Fisch"}

# Adding a new key-value pair to the dictionary
worterbuch["Vogel"] = "Bird"

# Accessing values using keys
print("Schildkröte =", worterbuch["Schildkröte"])
print("Vogel =", worterbuch["Vogel"])

print("-------------dictionary-------------")
dictionary = {
    "Cat": "Katze",
    "Dog": "Hund",
    "Turtle": "Schildkröte",
    "Fish": "Fisch",
    "Book": "Buch",
}

# Adding a new key-value pair to the dictionary
dictionary["Bird"] = "Vogel"

# Accessing values using keys
print("Turtle =", dictionary["Turtle"])
print("Bird =", dictionary["Bird"])

# Removing a key-value pair from the dictionary
del dictionary["Book"]
print(dictionary)
