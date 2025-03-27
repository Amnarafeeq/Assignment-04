def sub_seven(num: int) -> str:
    """Subtracts 7 from the given number and returns the result as a formatted string."""
    return f"After subtracting 7, the result is: {num - 7}"

def main():
    """Handles user input, ensures validation, and prints the result."""
    while True:
        try:
            num = int(input("Enter a number: "))
            print(sub_seven(num))
            break  # Exit loop after successful input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
