# Define the maximum value for the Fibonacci sequence
max_val = 10000

# Function to generate Fibonacci numbers up to max_val
def fibonacci():
    a = 0  # First number in the sequence
    b = 1  # Second number in the sequence
    
    # Loop until the value of 'a' exceeds max_val
    while a <= max_val:
        print(a, end=" ")  # Print the current number
        
        # Calculate the next Fibonacci number
        c = a + b
        a = b  # Move 'b' to 'a'
        b = c  # Move new value to 'b'

# Call the function to generate and print the Fibonacci sequence
fibonacci()
