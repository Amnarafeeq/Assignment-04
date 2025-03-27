import random
import time

def print_banner():
    print("\n" + "="*50)
    print("      🎭 Welcome to the Ultimate Mad Libs! 🎭")
    print("="*50 + "\n")


random_nouns = ["unicorn 🦄", "spaceship 🚀", "robot 🤖", "dragon 🐉", "alien 👽"]
random_verbs = ["dance 💃", "jump 🤸", "sing 🎤", "fly ✈️", "swim 🏊"]
random_adjectives = ["crazy 🤪", "funny 😂", "amazing 😍", "weird 🌀", "magical ✨"]
random_places = ["Lahore 🌆", "Karachi 🏖️", "Islamabad 🏔️", "Murree ❄️", "Hunza Valley ⛰️", "Skardu 🏔️", "Fairy Meadows 🌿", "Gwadar 🌊", "Thar Desert 🏜️", "Kaghan Valley 🌄"]


stories = [
    """
    🌟 Once upon a time, {name} traveled to {place}. As they arrived, they saw a {adjective} {noun} standing in the middle of the road! 😱
    The {noun} looked at {name} and whispered, "Do you want to {verb} with me?" 🤔

    Without thinking twice, {name} shouted, "Of course!" 🎉 So, they both started to {verb} all around {place}.
    Suddenly, a portal appeared and sucked them into a magical world! 🌍✨

    There, they found a treasure chest full of {adjective} surprises! 🎁
    It was the best adventure of {name}'s life! 🚀💫
    """,

    """
    🎭 One fine morning, {name} woke up and found a {adjective} {noun} sitting at the edge of their bed! 😲
    It had glowing eyes and was holding a tiny sign that said, "Let's {verb} together in {place}!" 🎫

    Confused but excited, {name} followed the {noun} into a secret tunnel that led straight to {place}! 🚇

    As they reached, they saw a giant festival happening! 🎆🎪
    Everyone was {verb} and laughing! 🤩

    {name} realized that this was the most {adjective} day of their life! 🎉
    """
]

def get_input(prompt, random_list):
    user_input = input(prompt)
    return user_input if user_input else random.choice(random_list)

def play_mad_libs():
    print_banner()

    name = input("Enter a name: ") or "Alex"
    place = get_input("Enter a place: ", random_places)
    adjective = get_input("Enter an adjective: ", random_adjectives)
    noun = get_input("Enter a noun: ", random_nouns)
    verb = get_input("Enter a verb: ", random_verbs)

    story = random.choice(stories).format(name=name, place=place, adjective=adjective, noun=noun, verb=verb)

    print("\nGenerating your adventure...\n")
    time.sleep(2)
    print("📖 Here’s your crazy Mad Libs story! 📖\n")
    print(story)

    again = input("\nWant to play again? (yes/no): ").strip().lower()
    if again == "yes":
        play_mad_libs()
    else:
        print("\nThanks for playing! 🎉 Have a fun day! 😃\n")

play_mad_libs()