def sqr_number():
    # Ask the user to enter a number
    number: float = float(input("Enter a number: "))

    # Calculate the square of the number
    square: float = number ** 2

    # Display the squared result
    print(f"The square of {number} is {square}")

# Run the function if the script is executed directly
if __name__ == "__main__":  
    sqr_number()
