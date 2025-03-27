def double_number(num: int):
    """
    Function to double the given number.
    """
    result = num * 2  # Multiply the number by 2
    return f"Double that is {result}"  # Return the formatted result

# Prompt user for input
num = int(input("Enter a number to double: "))

# Call the function and display the result
print(double_number(num))
