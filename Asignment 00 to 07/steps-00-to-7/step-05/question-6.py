# Function to repeatedly double a number until it reaches or exceeds 100
def double_value():
    # Take user input and convert it to an integer
    curr_value = int(input("Enter a number: "))

    # Keep doubling the value while it's less than 100
    while curr_value < 100:
        curr_value *= 2  # Double the current value
        print(curr_value)  # Print the updated value

# Call the function to execute the doubling process
double_value()
