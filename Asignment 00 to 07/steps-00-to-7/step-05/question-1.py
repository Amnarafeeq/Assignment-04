# Import random module to generate a random number
import random

# Function to play a number guessing game
def guess_number():
    # Generate a random number between 1 and 99
    numbers = random.randint(1, 99)

    while True:
        try:
            # Prompt user to guess the number
            enter_number = int(input("Guess a number between 1 to 99: "))
        except ValueError:
            print("Enter a valid number.")  # Handle invalid input (e.g., letters)
            continue  # Restart the loop
        
        # Check if the guessed number is too high
        if enter_number > numbers:
            print("Your guess is too high.")
        # Check if the guessed number is too low
        elif enter_number < numbers:
            print("Your guess is too low.")
        # If the guess is correct, exit the loop
        else:
            print("Congratulations! You guessed the right number.")
            break  # Exit the loop when guessed correctly

# Run the guessing game
guess_number()
