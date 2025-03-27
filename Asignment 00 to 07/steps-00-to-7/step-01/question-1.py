import random  # Import the random module for generating random numbers

# Function to roll two dice and display the result
def roll_dice():
    turn1: int = random.randint(1, 6)  # Roll the first die (random number between 1 and 6)
    turn2: int = random.randint(1, 6)  # Roll the second die (random number between 1 and 6)
    result: int = turn1 + turn2  # Calculate the total result
    print(f'You rolled {turn1} + {turn2} = {result}')  # Print the rolled values and their sum

# Main function to demonstrate the dice rolling
def main():
    dice1: int = 10  # Define a variable in the main function

    print(f"die1 in main() before calling roll_dice() is {dice1}\n")  # Print the initial value of dice1

    roll_dice()  # Call the function to roll dice
    roll_dice()  
    roll_dice()  

    print(f"\ndie1 in main() after calling roll_dice() is {dice1}")  # Print the value of dice1 after rolling

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
