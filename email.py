class Email:
    def __init__(self, email_address, subject_line, email_content):
        # Store the email details
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Email is unread by default

    def mark_as_read(self):
        # Mark the email as read
        self.has_been_read = True
        print(f"\nEmail from {self.email_address} marked as read.\n")

def populate_inbox():
    # Create some sample emails and add them to the inbox
    email1 = Email("john.doe@example.com", "Welcome to HyperionDev!", "Hello, welcome to the HyperionDev platform!")
    email2 = Email("admin@example.com", "Great work on the bootcamp!", "You've done an excellent job in the bootcamp!")
    email3 = Email("grades@example.com", "Your excellent marks!", "Congrats on achieving excellent marks in the course!")
    inbox.append(email1)
    inbox.append(email2)
    inbox.append(email3)

def list_emails():
    # List all emails with their index number
    if len(inbox) == 0:
        print("\nNo emails in inbox.")
    else:
        print("\nInbox:")
        for i, email in enumerate(inbox):
            status = "Read" if email.has_been_read else "Unread"
            print(f"{i} - {email.subject_line} ({status})")

def read_email(index):
    # Read the email at the given index
    if index >= 0 and index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
    else:
        print("\nInvalid email index!")

def view_unread_emails():
    # Show only unread emails
    unread_found = False
    for email in inbox:
        if not email.has_been_read:
            print(f"- {email.subject_line}")
            unread_found = True
    if not unread_found:
        print("\nNo unread emails.")

def main():
    global inbox  # To access the inbox from other functions
    inbox = []  # Start with an empty inbox
    populate_inbox()  # Add sample emails to the inbox

    while True:
        # Show the menu to the user
        print("\n--- Email Simulator ---")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")

        # Get the user's choice
        choice = input("Please select an option (1/2/3): ")

        if choice == "1":
            list_emails()
            try:
                email_index = int(input("Enter the index of the email you want to read: "))
                read_email(email_index)
            except ValueError:
                print("\nPlease enter a valid number for the index.")
        elif choice == "2":
            view_unread_emails()
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

#Code was written By Jack Hughes For the purpose of Task 9

