# pattern.py

# This program prints an arrow pattern

# Loop through numbers from 1 to 9
for i in range(1, 10):
    if i <= 5:
        # Print stars increasing from 1 to 5
        print('*' * i)
    else:
        # Print stars decreasing from 4 to 1
        print('*' * (10 - i))
