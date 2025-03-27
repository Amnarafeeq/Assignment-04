def double_number(num: int):
    """
    Doubles the number repeatedly until it reaches or exceeds 100.
    Prints each doubled value.
    """
    curr_num = num  # Initialize current number with the input value

    # Loop to keep doubling the number until it reaches or exceeds 100
    while curr_num < 100:
        curr_num = curr_num * 2  # Multiply by 2
        print(curr_num)  # Print the updated value

# Get user input and convert it to an integer
num = int(input("Enter number: "))

# Call the function with the user-provided number
double_number(num)
