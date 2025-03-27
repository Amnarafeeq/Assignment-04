# Import sha256 from hashlib to securely hash passwords
from hashlib import sha256  

# Function to verify login credentials
def login(email, stored_login, password_to_check):
    # Check if the entered email exists and its hashed password matches the stored hash
    if email in stored_login and stored_login[email] == hash_password(password_to_check):
        return True  # Login successful
    return False  # Login failed

# Function to hash a password using SHA-256
def hash_password(password):
    return sha256(password.encode()).hexdigest()  # Convert password to hash

# Main function to simulate user login
def main():
    # Dictionary storing emails and their corresponding hashed passwords
    stored_login = {
        "amna@gmail.com": hash_password("amna123"),
        "user@example.com": hash_password("password123"),
        "admin@site.com": hash_password("admin456")
    }

    # Prompt user for login credentials
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    # Check if login credentials are valid
    if login(email, stored_login, password):  # Fixed variable name from "password" to "password_to_check"
        print("Login Successful.")
    else:
        print("Invalid email or password!")    

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()
