import random

def guess_number():
    while True:  # Game restart option
        print("\n" + "=" * 50)
        print("🎮 Welcome to the Number Guessing Game! 🎲")
        print("=" * 50 + "\n")

        number = random.randint(1, 50)  # Generate random number
        attempts = 5  # Set max attempts

        while attempts > 0:
            try:
                user_input = int(input(f"🔢 Enter your guess (1-50) | Attempts left: {attempts} ➡ "))
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
                continue

            if user_input == number:
                print(f"🎉 Congratulations! You guessed the number {number} correctly! 🏆🥳")
                break
            elif user_input < number:
                print(f"🔻 Too low! Try again. 📉")
            else:
                print("🔺 Too high! Try again. 📈")

            attempts -= 1  # Reduce attempts

        if attempts == 0:
            print(f"💀 Oh no! You're out of attempts! The correct number was {number}. 😢")

        # Play Again Option
        play_again = input("🔄 Do you want to play again? (🟢Y / 🔴N): ").lower()
        if play_again != "y":
            print("👋 Thanks for playing! Have a great day! 😊✨")
            break  # Exit game loop

guess_number()

