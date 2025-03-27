import random  # Import the random module to randomly select a story

def tiny_madlib():
    # Get user inputs for a noun, verb, and adjective
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")

    # List of funny madlib-style stories with placeholders for user inputs
    stories = [
        f"The \033[1;3m{noun}\033[0m tried to \033[1;3m{verb}\033[0m but ended up stuck in a \033[1;3m{adjective}\033[0m tree! 🌳😂",
        f"A \033[1;3m{noun}\033[0m wanted to \033[1;3m{verb}\033[0m, but its \033[1;3m{adjective}\033[0m pants fell off! 👖🤣",
        f"The \033[1;3m{noun}\033[0m was \033[1;3m{verb}\033[0m when suddenly a \033[1;3m{adjective}\033[0m chicken attacked! 🐔😆",
        f"A \033[1;3m{noun}\033[0m decided to \033[1;3m{verb}\033[0m, but tripped over a \033[1;3m{adjective}\033[0m banana peel! 🍌🤦‍♂️",
        f"The \033[1;3m{noun}\033[0m went to \033[1;3m{verb}\033[0m, but a \033[1;3m{adjective}\033[0m squirrel stole its lunch! 🐿️😂"
    ]

    # Randomly select and display one of the madlib stories
    print("\n", random.choice(stories)) 

# Run the function when the script is executed
if __name__ == "__main__":
    tiny_madlib()
