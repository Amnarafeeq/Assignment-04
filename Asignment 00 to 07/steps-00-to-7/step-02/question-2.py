def double_numbers(numbers):
    res = []  # Create an empty list to store results
    for num in numbers:
        res.append(num * 2)  # Append the doubled number to the list
    return res  # Return the updated list

if __name__ == '__main__':
    print(double_numbers([1, 2, 3, 4, 5]))  
