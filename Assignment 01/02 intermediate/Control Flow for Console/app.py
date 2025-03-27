import random  # Import random module to generate random numbers

def high_low_game():
    """
    A simple high-low game where the player guesses if their number 
    is higher or lower than the computer's number.
    """
    score = 0  # Initialize player's score
    total_rounds = 5  # Set the total number of rounds

    print("\n🎮 **Welcome to the High-Low Game!** 🎮")
    
    # Loop through each round
    for i in range(1, total_rounds + 1):  
        print(f"\n🔵 **Round {i} of {total_rounds}** 🔵")
        
        # Generate random numbers for player and computer
        computer_num = random.randint(1, 100)
        user_num = random.randint(1, 100)

        # Display player's number
        print("\n🎲 **High-Low Game** 🎲")
        print(f"🔹 **Your Number:** {user_num}")
        
        # Ask the player for their guess
        guess = input("\n🔍 Do you think your number is **higher** or **lower** than the computer's number? (Type 'higher' or 'lower'): ").strip().lower()
        
        # Check if the player's guess is correct
        if (guess == "higher" and user_num > computer_num) or (guess == "lower" and user_num < computer_num):
            print(f"\n✅ **Correct!** The computer's number was {computer_num}. You earned a point! 🎉")
            score += 1  # Increase score if the player guessed correctly
        else:
            print(f"\n❌ **Wrong!** The computer's number was {computer_num}. Better luck next time!")

    # Display final score after all rounds
    print(f"\n🏆 **Game Over! Your Final Score: {score} / {total_rounds}** 🏆")

# Run the game
high_low_game()
