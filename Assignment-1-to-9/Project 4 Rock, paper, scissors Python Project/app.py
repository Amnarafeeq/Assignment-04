import random

def play_game():
    print("*"* 50, "\n")
    print("🎮 Welcome to *Rock, Paper, Scissors!* ✂️📄🪨")
    print("\n","*"* 50)

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("🔹 Enter your choice (Rock, Paper, Scissors): ").lower()

        if user_choice not in choices:
            print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("🤝 *It's a Tie!* 😃\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("🎉 *You Win!* 🏆🔥\n")
        else:
            print("❌ *Computer Wins!* Better luck next time! 😢\n")

        play_again = input("🔄 Do you want to play again? (Y/N): ").lower()
        if play_again != "y":
            print("\n👋 *Thanks for playing!* Have a great day! 😊✨\n")
            break

play_game()
