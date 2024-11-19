sentence = "Lorem Ipsum Dolor Sit Amet Consectetur Adipiscing Elit"
words = sentence.split()
words.sort()

# Reverse the order of words for descending alphabetical order
words.reverse()

# Print each word in the reversed list
for word in words:
    print(word)
