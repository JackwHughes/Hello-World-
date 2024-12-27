# Create a file named while.py
# File content:

# Initialize variables to keep track of the sum, count, and user input
sum_of_numbers = 0
count_of_numbers = 0

print("Enter numbers to calculate the average. Enter -1 to stop. (0 is not valid)")

while True:
    try:
        user_input = int(input("Enter a number: "))

        # Exit the loop if the user enters -1
        if user_input == -1:
            break

        # Ignore 0 as it's not a valid input
        if user_input == 0:
            print("0 is not a valid number. Please try again.")
            continue

        # Add the number to the sum and increment the count
        sum_of_numbers += user_input
        count_of_numbers += 1

    except ValueError:
        print("Invalid input. Please enter an integer.")

# Calculate and display the average if there are valid inputs
if count_of_numbers > 0:
    average = sum_of_numbers / count_of_numbers
    print(f"The average of the valid numbers entered is: {average}")
else:
    print("No valid numbers were entered to calculate an average.")

# Code was written by me Jack Hughes for the purpose of Task 3