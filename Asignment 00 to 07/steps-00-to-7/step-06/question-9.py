def make_sentence(word, part_of_speech):
    """
    Function to generate a sentence based on the given word and part of speech category.
    
    part_of_speech:
    - 0 → Greeting sentence
    - 1 → Self-introduction sentence
    - 2 → Encouragement sentence
    """
    if part_of_speech == 0:
        print(f"Hello {word}, it's nice to meet you!")  # Greeting sentence
    elif part_of_speech == 1:
        print(f"I'm {word}, and I love learning new things.")  # Self-introduction sentence
    elif part_of_speech == 2:
        print(f"You are {word}, and you are doing great!")  # Encouragement sentence
    else:
        print("Error: Please enter 0, 1, or 2.")  # Error message for invalid input

# Get user input
word = input("Type a word: ")  
part_of_speech = int(input("Type 0, 1, or 2: "))  

# Call the function to generate a sentence
make_sentence(word, part_of_speech)
