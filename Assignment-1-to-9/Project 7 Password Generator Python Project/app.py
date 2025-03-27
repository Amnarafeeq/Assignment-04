import string
import random

def generate_password():
    print("\n🔐 Welcome to the Secure Password Generator! 🔐\n")

    length = int(input("📏 Enter the desired password length (minimum 4): "))

    if length < 4:
        print("⚠️ Password length must be at least 4 characters. Try again!")
        return

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    all_characters = uppercase_letters + lowercase_letters + digits + punctuation

    print("\n🛠 Generating a **strong** password for you... Please wait! ⏳")

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(punctuation)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    final_password = "".join(password)

    print("\n✅ Your **secure** password is ready: 🔑")
    print(f"\n🔒 **{final_password}** 🔒\n")
    print("💡 Tip: Save it in a secure place! 🛡️")

generate_password()

