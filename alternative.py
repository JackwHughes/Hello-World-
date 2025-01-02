# Program to alternate characters and words in a string

# Function to change alternate characters to uppercase and lowercase
def alternate_characters(string):
    """Takes a string and alternates its characters between uppercase and lowercase."""
    result = ""  # This will hold the final output
    for index, char in enumerate(string):
        if char.isalpha():  # Only change alphabetic characters
            if index % 2 == 0:  # Even index
                result += char.upper()
            else:  # Odd index
                result += char.lower()
        else:
            result += char  # Keep spaces and punctuation as is
    return result

# Function to change alternate words to uppercase and lowercase
def alternate_words(string):
    """Takes a string and alternates its words between uppercase and lowercase."""
    words = string.split()  # Split the string into a list of words
    for index, word in enumerate(words):
        if index % 2 == 0:  # Even index
            words[index] = word.lower()
        else:  # Odd index
            words[index] = word.upper()
    return " ".join(words)  # Join the words back into a single string

# Main program starts here
if __name__ == "__main__":
    # Ask the user to enter a string
    input_string = input("Enter a string: ")

    # Process the string to alternate characters
    char_result = alternate_characters(input_string)
    print("\nString with alternate characters in uppercase and lowercase:")
    print(char_result)

    # Process the string to alternate words
    word_result = alternate_words(input_string)
    print("\nString with alternate words in lowercase and uppercase:")
    print(word_result)


# Code was written by me Jack Hughes for the purpose of Task 7