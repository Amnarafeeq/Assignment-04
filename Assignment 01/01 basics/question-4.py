import random  # Import the random module to generate random numbers

def guess_random_number():
    """
    A number guessing game where the user has to guess a randomly generated number
    between 1 and 99.
    """
    guess_num = random.randint(1, 99)  # Generate a random number between 1 and 99

    while True:
        try:
            # Prompt the user to enter a number
            enter_num = int(input("Enter a number between 1 to 99: "))
        except ValueError:
            # Handle cases where input is not a valid integer
            print("Please enter a number only.")
            continue  # Restart the loop if input is invalid

        if enter_num > guess_num:
            print("Your guess is too high.")  # Inform the user if the guess is too high
        elif enter_num < guess_num:
            print("Your guess is too low.")  # Inform the user if the guess is too low
        else:
            print("Congratulations! You guessed the right number.")  # Correct guess message
            break  # Exit the loop when the correct number is guessed

# Call the function to start the game
guess_random_number()
