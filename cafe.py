# List of items that the café sells
menu = ['Coffee', 'Tea', 'Cake', 'Sandwich']

# Dictionary for the stock of each item (how many items we have)
stock = {
    'Coffee': 30,
    'Tea': 20,
    'Cake': 15,
    'Sandwich': 25
}

# Dictionary for the price of each item
price = {
    'Coffee': 2.50,
    'Tea': 1.80,
    'Cake': 3.00,
    'Sandwich': 4.50
}

# I will calculate the total worth of the stock
total_worth = 0

# Loop through each item in the menu
for item in menu:
    # Multiply the stock quantity by the price to get the value of each item
    item_value = stock[item] * price[item]
    # Add this value to the total worth of the stock
    total_worth += item_value

# Now I will print out the total worth of the stock
print("The total worth of the stock in the café is: $" + str(round(total_worth, 2)))


# Code was written by me Jack Hughes for the purpose of Task 7