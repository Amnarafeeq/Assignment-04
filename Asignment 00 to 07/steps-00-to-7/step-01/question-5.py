def find_quotient_remainder():
    dividend: int = int(input("Enter the dividend: "))  # Get the dividend from the user
    divisor: int = int(input("Enter the divisor: "))    # Get the divisor from the user

    quotient: int = dividend // divisor  # Perform integer division to get the quotient
    remainder: int = dividend % divisor  # Get the remainder using modulus operator

    # Display the quotient and remainder with formatting (bold & italic)
    print(f"The result of this division is \033[1;3m{quotient}\033[0m with a remainder of \033[1;3m{remainder}\033[0m")

# Run the function if the script is executed directly
if __name__ == "__main__":
    find_quotient_remainder()
