import random

# Probability of stopping early
DONE_LIKELIHOOD = 0.2  

# Function that randomly decides whether to stop counting
def done():
    if random.random() < DONE_LIKELIHOOD:  # Generates a random number between 0 and 1
        return True  # If the number is less than 0.2, stop counting
    return False  # Otherwise, continue counting

# Function to count from 1 to 10, but might stop early
def chaotic_counting():
    for i in range(10):  # Loop through numbers 1 to 10
        curr_num = i + 1  # Get current number
        if done():  # Check if we should stop
            return  # Stop the function early
        print(curr_num)  # Print the current number

# Main function to execute the chaotic counting
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")       
    chaotic_counting()  # Call the chaotic counting function
    print("I'm done.")  # Print final message

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
