import random

def play_hangman():
    random_words = ["java", "python", "typescript", "hangman", "developer"]

    while True: 
        choice = random.choice(random_words) 
        blanks = list("_" * len(choice))  
        attempts = 6  
        guessed_letters = []  

        print("\n🎮 Welcome to Hangman! 🎭\n")

        while attempts > 0 and "_" in blanks:  
            print(" ".join(blanks) + "\n")  
            print(f"🔢 Attempts Left: {attempts}")

            guessed_letter = input("Guess a letter: ").lower()

            if guessed_letter in guessed_letters:
                print("⚠️ You already guessed this letter! Try another one.")
                continue

            guessed_letters.append(guessed_letter)  

            if guessed_letter in choice:
                print("✅ Correct!")
                for index in range(len(choice)):
                    if choice[index] == guessed_letter:
                        blanks[index] = guessed_letter  
            else:
                print("❌ Wrong guess!")
                attempts -= 1  

            if "_" not in blanks:
                print("\n🎉 Congratulations! You guessed the word:", choice)
                break

        if attempts == 0:
            print("\n💀 Game Over! The word was:", choice)

        play_again = input("🔄 Do you want to play again? (Y/N): ").lower()
        if play_again != "y":
            print("\n👋 *Thanks for playing!* Have a great day! 😊✨\n")
            break  

play_hangman()
