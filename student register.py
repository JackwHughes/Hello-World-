# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open the file in write mode
with open("reg_form.txt", "w") as file:
    # Loop through the number of students
    for i in range(num_students):
        # Ask for the student ID
        student_id = input(f"Enter the ID for student {i + 1}: ")
        # Write the student ID to the file with a dotted line
        file.write(student_id + " ..........\n")

print("Registration complete! The reg_form.txt file has been created.")


#code written by jack hughes for the the purposr of task 8