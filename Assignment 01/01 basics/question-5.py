import random  # Import the random module to generate random numbers

def print_random_nums():
    """
    Prints 10 random numbers between 1 and 99 in a single line.
    """
    for _ in range(10):  # Loop 10 times to generate 10 random numbers
        print(random.randint(1, 99), end=" ")  # Generate and print a random number with a space separator

# Call the function to execute it
print_random_nums()
