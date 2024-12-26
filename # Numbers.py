Numbers.py

# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate and print the sum of all the numbers
sum_of_numbers = num1 + num2 + num3
print("Sum of all the numbers:", sum_of_numbers)

# Calculate and print the first number minus the second number
difference = num1 - num2
print("First number minus the second number:", difference)

# Calculate and print the third number multiplied by the first number
product = num3 * num1
print("Third number multiplied by the first number:", product)

# Calculate and print the sum of all three numbers divided by the third number
if num3 != 0:  # Avoid division by zero
    division_result = sum_of_numbers / num3
    print("Sum of all three numbers divided by the third number:", division_result)
else:
    print("Error: Division by zero is not allowed!")


# Code was written by me Jack Hughes for the purpose of Task 3
