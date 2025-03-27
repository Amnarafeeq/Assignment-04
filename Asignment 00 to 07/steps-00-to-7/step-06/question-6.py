def is_odd():
    """
    Function to check if numbers from 0 to 9 are odd.
    Prints True if odd, False if even.
    """
    for i in range(10):  # Loop through numbers 0 to 9
        if i % 2 != 0:  # Check if the number is odd
            print(True)  # Print True for odd numbers
        else:
            print(False)  # Print False for even numbers

# Call the function to execute
is_odd()
