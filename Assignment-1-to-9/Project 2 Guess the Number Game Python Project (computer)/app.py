import random  

def computer_guess():
    while True:
        low = 1
        high = 100  
        attempts = 5
        print("=" * 50, "\n")
        print("    🎮✨ *New Game Started!* ✨🎮   ")
        print("\n", "=" * 50)

        while attempts > 0:
            number = random.randint(low, high)  
            print(f"🤖 Computer's Guess: 🎯 {number}")
            guess = input(f"📢 *Is {number} too high (🔺H), too low (🔻L), or correct (✅C)?* ").lower()
            attempts -= 1

            if guess == "h":
                high = number - 1
                print("🔴 *Too High!* 📉 Let me try a smaller number...\n")
            elif guess == "l":
                low = number + 1
                print("🟢 *Too Low!* 📈 Let me try a bigger number...\n")
            elif guess == "c":
                print(f"🎉🎉 *Hooray! I guessed your number {number} in {5 - attempts} attempts!* 🏆🥳\n")
                break
            else:
                print("❌ *Invalid Input!* Please enter 🔺H (High), 🔻L (Low), or ✅C (Correct).\n")
                attempts += 1

            if attempts == 0:
                print("💀 *Oh no! I ran out of attempts!* 😢 Better luck next time! 🎲\n")

        play_again = input("🔄 *Do you want to play again? (🟢Y / 🔴N):* ").lower()
        if play_again != "y":
            print("👋 *Thanks for playing!* Have a great day! 😊✨")
            break

computer_guess()