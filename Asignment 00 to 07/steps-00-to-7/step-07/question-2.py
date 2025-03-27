# Function to greet the user
def greet(name: str):
    """
    Prints a greeting message with the given name.
    """
    print(f"Greetings {name}!")

# Main function to take user input and call the greet function
def main():
    """
    Takes user input for their name and passes it to the greet function.
    """
    name: str = input("What's your name? : ")  # Prompt user for their name
    greet(name)  # Call the greet function

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
