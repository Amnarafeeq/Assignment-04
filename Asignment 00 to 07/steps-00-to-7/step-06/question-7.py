def print_divisors(num: int):
    """
    Function to print all divisors of a given number.
    """
    print("Here are the divisors of", num)

    for i in range(1, num):  # Loop through numbers from 1 to num-1
        curr_divisor = i + 1  # Get the actual divisor
        if num % curr_divisor == 0:  # Check if it's a divisor
            print(curr_divisor)  # Print the divisor

def main():
    """
    Main function to get user input and find divisors.
    """
    num = int(input("Enter a number to find its divisors: "))  # Get user input
    print_divisors(num)  # Call function to print divisors

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
