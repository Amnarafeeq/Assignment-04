# Function to calculate the average of two numbers
def find_average(num1: float, num2: float):
    sum_value = num1 + num2  # Add the two numbers
    return f"\nThe average of {num1} and {num2} is {sum_value / 2}"  # Calculate and return the average

# Taking user input for two numbers
num1: float = float(input("Enter first number: "))
num2: float = float(input("Enter second number: "))

# Calling the function and printing the result
print(find_average(num1, num2))
