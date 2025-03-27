def print_ones_digit(num: int):
    """
    Function to find and return the ones (last) digit of a given number.
    """
    return f"The ones digit is: {num % 10}"  # Extract the last digit using modulo 10

def main():
    """
    Main function to take user input and print the ones digit.
    """
    num = int(input("Enter a number: "))  # Get input from user
    print(print_ones_digit(num))  # Call function and display result

if __name__ == "__main__":
    main()  # Execute the main function when the script runs
