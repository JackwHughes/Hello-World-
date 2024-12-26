# manipulation.py

str_manip = input("Please enter a sentence: ")

# Calculate and display the length of str_manip
print("Length of the sentence:", len(str_manip))

# Find the last letter in str_manip and replace every occurrence of it with '@'
last_letter = str_manip[-1]  # Get the last letter of the sentence
str_manip_replaced = str_manip.replace(last_letter, '@')
print("Sentence with last letter replaced:", str_manip_replaced)

# Print the last three characters in str_manip backwards
last_three_backwards = str_manip[-3:][::-1]  # Extract last three chars and reverse them
print("Last three characters backwards:", last_three_backwards)

# Create a five-letter word from the first three characters and the last two characters
first_three = str_manip[:3]  # First three characters
last_two = str_manip[-2:]    # Last two characters
five_letter_word = first_three + last_two  # Combine to form the five-letter word
print("Five-letter word:", five_letter_word)


# Code was written by me Jack Hughes for the purpose of Task 3
