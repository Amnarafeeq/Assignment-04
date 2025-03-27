# Prompt message asking the user what they want
PROMPT = "What do you want? "

# Joke message that will be displayed if the user asks for a joke
JOKE = "Here is a joke for you! Why do Python programmers prefer dark mode? Because light attracts bugs! 🐞😂"

# Response message if the user requests something other than a joke
SORRY = "Sorry, I only tell jokes."

def joke_bot():
    """Function to take user input and respond with either a joke or a default message."""

    # Get user input, remove extra spaces, and convert to lowercase for case-insensitive comparison
    user_input = input(PROMPT).strip().lower()

    # Check if the user asked for a joke
    if user_input == "joke":
        print(JOKE)  # Print the joke
    else:
        print(SORRY)  # Print the default response

# Call the function to run the joke bot
joke_bot()
