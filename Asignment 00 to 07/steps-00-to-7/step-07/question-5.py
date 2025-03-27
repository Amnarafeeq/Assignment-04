# Function to get user info
def get_user_info():
    """
    Collects the user's first name, last name, and email.
    Returns them as a tuple.
    """
    first_name = input("What's your First Name? ").strip().title()  # Capitalize first letter
    last_name = input("What's your Last Name? ").strip().title()    # Capitalize first letter
    email = input("What's your email address? ").strip().lower()    # Convert email to lowercase for consistency
    return first_name, last_name, email

# Main function to display user data
def main():
    """
    Calls get_user_info() and prints the formatted user data.
    """
    first_name, last_name, email = get_user_info()
    print("\n✅ Received the following user data:")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Email: {email}")

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
