# Define a constant affirmation string
AFFIRMATION: str = "I am capable of doing anything I put my mind to."

# Function to prompt the user to type the affirmation correctly
def write_affirmation():
    # Display the affirmation prompt
    print(f'Please type the following affirmation: "{AFFIRMATION}"')

    # Take user input
    user_type: str = input()

    # Loop until the user correctly types the affirmation
    while user_type != AFFIRMATION:
        print("That's not the affirmation. Please try again.")

        # Re-prompt the user to type the correct affirmation
        print(f'Please type the following affirmation: "{AFFIRMATION}"')
        user_type: str = input()

    print("That's the right affirmation. Well done! 🎉")

# Call the function to execute the affirmation typing task
write_affirmation()
