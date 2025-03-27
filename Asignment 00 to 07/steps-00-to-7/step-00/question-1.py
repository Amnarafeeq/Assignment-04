def add():
    # Take first number as input (string) and convert it to an integer
    num1: str = input("Enter the first number: ")  
    num1 = int(num1)  
    
    # Take second number as input (string) and convert it to an integer
    num2: str = input("Enter the second number: ")
    num2 = int(num2)
    
    # Calculate the sum of both numbers
    sum = num1 + num2  
    
    # Print the result
    print(f"The sum of {num1} and {num2} = {sum}")  

# Run the function if the script is executed directly
if __name__ == "__main__":
    add()
