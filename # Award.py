# Award.py

# Ask the user to enter the times for each of the three events
swimming_time = float(input("Enter the swimming time in minutes: "))
cycling_time = float(input("Enter the cycling time in minutes: "))
running_time = float(input("Enter the running time in minutes: "))

# Calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

# Display the total time
print(f"Total time taken: {total_time} minutes")

# Determine the award based on the total time
if total_time <= 100:
    award = "Honorary colours"
elif total_time <= 105:
    award = "Honorary half colours"
elif total_time <= 110:
    award = "Honorary scroll"
else:
    award = "No award"

# Display the award
print(f"Award: {award}")


# Code was written by me Jack Hughes for the purpose of Task 3