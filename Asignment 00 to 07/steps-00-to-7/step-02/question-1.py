def sum_numbers(numbers: int):  # Function to sum up all numbers in a list
    i = 0  # Initialize sum variable
    
    for num in numbers:  # Loop through each number in the list
        i += num  # Add the current number to the sum
    
    return i  # Return the final sum

 
if __name__ == '__main__':  
    print(sum_numbers([1, 2, 3, 4, 5]))  # Call the function with a list of numbers and print the result
