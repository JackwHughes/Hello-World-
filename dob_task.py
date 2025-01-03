# Open the DOB.txt file and read its contents
file = open('DOB.txt', 'r')
lines = file.readlines()
file.close()

# Create lists for names and birthdates
names = []
birthdates = []

# Loop through each line in the file
for line in lines:
    parts = line.strip().split(' - ')  # Split each line at the ' - ' part
    if len(parts) == 2:  # Only add if it splits into exactly two parts
        names.append(parts[0])
        birthdates.append(parts[1])

# Print names
print("Name")
for name in names:
    print(name)

# Print birthdates
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)


