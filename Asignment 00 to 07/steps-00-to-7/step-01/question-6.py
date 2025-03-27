import random  # Import the random module to generate random numbers

num_side = 6  # Define the number of sides on a dice

def roll_dice():
    dice1 = random.randint(1, num_side)  # Roll the first dice (random number between 1 and 6)
    dice2 = random.randint(1, num_side)  # Roll the second dice
    total_of_dice = dice1 + dice2  # Calculate the total of both dice

    # Display the results with bold & italic formatting
    print(f"The first dice rolled a \033[1;3m{dice1}\033[0m.")
    print(f"The second dice rolled a \033[1;3m{dice2}\033[0m.")
    print(f"The total of the two dice is \033[1;3m{total_of_dice}\033[0m.")

# Run the function if the script is executed directly
if __name__ == "__main__":
    roll_dice()
