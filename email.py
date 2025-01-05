# Email class definition for creating email objects.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Constructor to initialize an email object.

        :param email_address: str - The sender's email address.
        :param subject_line: str - The subject line of the email.
        :param email_content: str - The content of the email.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Initialize the email as unread.

    def mark_as_read(self):
        """
        Mark the email as read by setting the has_been_read flag to True.
        """
        self.has_been_read = True


# Initialize an empty list called inbox to store email objects.
inbox = []

# Example code for testing (optional for manual verification)
if __name__ == "__main__":
    # Create email objects
    email1 = Email("sender1@example.com", "Meeting Update", "The meeting has been rescheduled.")
    email2 = Email("sender2@example.com", "System Alert", "Your system requires an update.")

    # Add email objects to the inbox
    inbox.append(email1)
    inbox.append(email2)

    # Print initial read statuses
    print(f"Email 1 read status: {email1.has_been_read}")  # Output: False
    print(f"Email 2 read status: {email2.has_been_read}")  # Output: False

    # Mark the first email as read
    email1.mark_as_read()

    # Print updated read statuses
    print(f"Email 1 read status: {email1.has_been_read}")  # Output: True
    print(f"Email 2 read status: {email2.has_been_read}")  # Output: False

