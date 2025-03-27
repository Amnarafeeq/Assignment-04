import random  # Import the random module to generate random numbers

# Function to generate and print 10 random numbers
def get_random_nums():
    for _ in range(10):  # Loop 10 times to generate 10 random numbers
        gen_nums = random.randint(1, 100)  # Generate a random number between 1 and 100
        print(gen_nums, end=" ")  # Print the number on the same line with a space

# Call the function to execute it
get_random_nums()        
